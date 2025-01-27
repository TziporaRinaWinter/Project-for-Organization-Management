from fastapi import APIRouter, Depends, HTTPException
from bl.widow_bl import WidowBL
from dal.widow_dal import WidowDAL
from db.DB_manager import DBManager

router = APIRouter()
db_manager = DBManager()


@router.get("/widows/")
def get_all_widows():
    widow_dal = WidowDAL(db_manager)
    widow_bl = WidowBL(widow_dal)
    return widow_bl.get_all_widows()

@router.get("/widows/{widow_id}")
def get_widow(widow_id: int):
    widow_dal = WidowDAL(db_manager)
    widow_bl = WidowBL(widow_dal)
    widow = widow_bl.get_widow(widow_id)
    if not widow:
        raise HTTPException(status_code=404, detail="Widow not found")
    return widow

@router.get("/widows.rel/{widow_id}")
def get_widow_with_rel(widow_id: int):
    widow_dal = WidowDAL(db_manager)
    widow_bl = WidowBL(widow_dal)
    widow = widow_bl.get_widow_with_rel(widow_id)
    if not widow:
        raise HTTPException(status_code=404, detail="Widow not found")
    return widow

@router.post("/widows/")
def create_widow(widow_data: dict):
    widow_dal = WidowDAL(db_manager)
    widow_bl = WidowBL(widow_dal)
    return widow_bl.create_widow(widow_data)

@router.put("/widows/{widow_id}")
def update_widow(widow_id: int, widow_data: dict):
    widow_dal = WidowDAL(db_manager)
    widow_bl = WidowBL(widow_dal)
    updated_widow = widow_bl.update_widow(widow_id, widow_data)
    if not updated_widow:
        raise HTTPException(status_code=404, detail="Widow not found")
    return updated_widow

@router.delete("/widows/{widow_id}")
def delete_widow(widow_id: int):
    widow_dal = WidowDAL(db_manager)
    widow_bl = WidowBL(widow_dal)
    deleted_widow = widow_bl.delete_widow(widow_id)
    if not deleted_widow:
        raise HTTPException(status_code=404, detail="Widow not found")
    return {"detail": "Widow deleted successfully"}

@router.delete("/widows/")
def delete_all_widows():
    widow_dal = WidowDAL(db_manager)
    widow_bl = WidowBL(widow_dal)
    widow_bl.delete_all_widows()
    return {"detail": "All widows deleted successfully"}
