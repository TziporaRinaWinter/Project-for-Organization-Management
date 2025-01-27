# כמובן! הנה דוגמה מקצה לקצה של יצירת טבלאות, שליפת נתונים וייצוג אובייקטים לפי המחלקה `ObjectManager` שסיפקת.

### 1. יצירת טבלאות

# נניח שיש לנו את המודלים הבאים:

# ```python
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Needy(Base):
    __tablename__ = 'needy'
    
    id = Column(Integer, primary_key=True)
    last_name = Column(String)
    children = relationship("Child", back_populates="needy")

class Child(Base):
    __tablename__ = 'children'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    needy_id = Column(Integer, ForeignKey('needy.id'))
    needy = relationship("Needy", back_populates="children")
# ```

### 2. יצירת אובייקטים

# כעת נשתמש ב-`ObjectManager` כדי ליצור אובייקטים:

# ```python
db_manager = DBManager()  # הנחה שיש לך מחלקה כזו
object_manager = ObjectManager(db_manager)

# יצירת טבלאות
object_manager.create_management_table(Needy)
object_manager.create_management_table(Child)

# יצירת אובייקט נצרך עם ילדים
needy_data = {
    "last_name": "Cohen",
    "children": [
        {"name": "David"},
        {"name": "Sarah"}
    ]
}

needy = object_manager.create_needy(needy_data)
# ```

### 3. שליפת נתונים

# כדי לשלוף את כל הנצרכים עם הילדים שלהם:

# ```python
needy_objects = object_manager.get_objects(Needy, NeedySchema, relationships=["children"])

for needy in needy_objects:
    print(f'Needy Last Name: {needy.last_name}')
    for child in needy.children:
        print(f'  Child Name: {child.name}')
# ```

### 4. עדכון אובייקטים

# נניח שאת רוצה לעדכן את שם המשפחה של נצרך:

# ```python
filters = [Needy.id == needy.id]
updates = {"last_name": "Levi"}

object_manager.update_objects(Needy, NeedySchema, filters, updates)
# ```

### 5. מחיקת אובייקטים

# כדי למחוק נצרך מסוים:

# ```python
filters = [Needy.id == needy.id]
object_manager.delete_objects(Needy, filters)
# ```

### סיכום

# הדוגמה הזו מציגה כיצד להשתמש במחלקת `ObjectManager` שלך כדי ליצור טבלאות, להוסיף אובייקטים, לשלוף נתונים, לעדכן ולמחוק אובייקטים. כל הפעולות מתבצעות באמצעות SQLAlchemy והמודלים שהגדרת.



from pydantic import BaseModel
from typing import List, Optional

class ChildSchema(BaseModel):
    id: Optional[int]
    name: str

class NeedySchema(BaseModel):
    id: Optional[int]
    last_name: str
    children: List[ChildSchema] = []

    class Config:
        orm_mode = True
