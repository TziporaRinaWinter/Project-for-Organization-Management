from copy import copy
from typing import Dict, List, Any, Type, TypeVar
from typing import Type, List, Any, TypeVar, Tuple, Optional, Dict
from sqlalchemy.orm import joinedload, selectinload

from pydantic import BaseModel

# from models.model import Needy, Address, Child
from sqlalchemy.sql import and_
from db.DB_manager import DBManager
from models.models import *
from models.schema import *
from sqlalchemy.orm import joinedload, selectinload
from models.schema import WidowSchema, AddressSchema, OrphanSchema, RelativeSchema, BankAccountSchema


class ObjectManager:

    def __init__(self, db_manager: DBManager):
        self.db_manager = db_manager

    def create_management_table(self, model_class):
        model_class.__table__.create(self.db_manager.engine, checkfirst=True)
    
    T = TypeVar("T", bound=BaseModel)

    def get_objects_whithout_rel(self, model_class, filters=None):
        """Retrieving records with the option for filters"""
        with self.db_manager.get_session() as session:
            query = session.query(model_class)
            if filters:
                query = query.filter_by(**filters)
            res = query.all()
            res_copy = [copy(widow) for widow in res]
            return res_copy

    def get_objects(
        self,
        base_table: Any,
        schema_class: Type[T],
        relationships: Optional[List[Any]] = None,
        filters: Optional[Dict[str, Any]] = None,
    ) -> List[T]:
        """
        Generic function for retrieving objects along with their relationships and converting them to Pydantic schemas.

        Args:
            base_table (Any): The table class for retrieval.
            schema_class (Type[T]): The Pydantic schema class for the main table.
            relationships (Optional[List[str]]): A list of relationship names for eager loading.
            filters (Optional[Dict[str, Any]]): A dictionary of filters for retrieval.

        Returns:
            List[T]: A list of objects translated to Pydantic schemas.
        """
        with self.db_manager.get_session() as session:

            query = session.query(base_table)

            if relationships:
                for relationship in relationships:
                    query = query.options(joinedload(getattr(base_table, relationship)))

            if filters:
                query = query.filter(and_(*filters))

            results = query.all()
            return [schema_class.from_orm(obj) for obj in results]

    def create_object(self, model_class, data: dict, relationships: dict = None, session=None):
        # Creating the main object
        obj_data = {key: data.get(key) for key in model_class.__table__.columns.keys()}
        obj = model_class(**obj_data)

        # If the session has not been transferred, we will use a new session.
        if session is None:
            with self.db_manager.get_session() as session:
                self._add_relationships(obj, relationships, session)
                session.add(obj)
                try:
                    session.commit()
                except Exception as e:
                    session.rollback()
                    raise e
        else:
            self._add_relationships(obj, relationships, session)
            session.add(obj)

        return obj

    def _add_relationships(self, obj, relationships, session):
        # Add relations if they exist
        if relationships:
            for relationship, (model_class, items) in relationships.items():
                if items:
                    for item_data in items:
                        related_obj = self.create_object(model_class, item_data, relationships=None, session=session)
                        if isinstance(getattr(obj, relationship), List):
                            getattr(obj, relationship).append(related_obj)
                        else:
                            setattr(obj, relationship, related_obj)

    def add_objects(self, obj_instances):
        """Adding a list of objects to a table"""
        with self.db_manager.get_session() as session:
            session.add_all(obj_instances)

    def add_object(self, obj_instance):
        with self.db_manager.get_session() as session:
            session.add(obj_instance)
        return obj_instance

    def update_objects(self, model_class, schema_class, filters, updates, rel=None):
        """Updating objects by filters, ignoring relations"""

        with self.db_manager.get_session() as session:
            query = session.query(model_class).filter(*filters)
            objects_to_update = query.all()

            print(objects_to_update)

            for obj in objects_to_update:
                for key, value in updates.items():
                    if hasattr(obj, key):
                        # התעלם מקשרים
                        if isinstance(getattr(obj, key), (list, dict)):
                            continue
                        # אם השדה הוא אובייקט פנימי, התעלם ממנו
                        if isinstance(value, dict) and not isinstance(getattr(obj, key), dict):
                            continue
                        # אם השדה הוא רשימה, התעלם ממנו
                        if isinstance(value, list):
                            continue
                        setattr(obj, key, value)

                session.add(obj)
            session.commit()
        return updates

    def update_object(self, model_class, obj_id, data: dict, relationships: dict = None):
        # Fetch the existing object
        with self.db_manager.get_session() as session:
            obj = session.query(model_class).filter(model_class.id == obj_id).first()
            if not obj:
                raise ValueError(f"{model_class.__name__} with id {obj_id} not found")

            # Update the main object fields
            for key in model_class.__table__.columns.keys():
                if key in data:
                    setattr(obj, key, data[key])

            # Update relationships if they exist
            self._update_relationships(obj, relationships, session)

            # Commit the changes
            session.add(obj)
            try:
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

            return obj
        
    def _update_relationships(self, obj, relationships, session):
        # Update relations if they exist
        if relationships:
            for relationship, (model_class, items) in relationships.items():
                # Clear existing relationships if needed
                current_relationships = getattr(obj, relationship)
                if isinstance(current_relationships, List):
                    current_relationships.clear()

                if items:
                    for item_data in items:
                        related_obj = self.create_object(model_class, item_data, relationships=None, session=session)
                        if isinstance(getattr(obj, relationship), List):
                            getattr(obj, relationship).append(related_obj)
                        else:
                            setattr(obj, relationship, related_obj)

    def delete_objects(self, model_class, filters):
        """Delete records by filters"""
        with self.db_manager.get_session() as session:
            query = session.query(model_class).filter(*filters)
            objects_to_delete = query.all()

            if not objects_to_delete:
                return False

            for obj in objects_to_delete:
                session.delete(obj)

            session.commit()
            return True

