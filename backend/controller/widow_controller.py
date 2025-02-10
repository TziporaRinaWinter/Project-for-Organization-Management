from fastapi import APIRouter, Depends, HTTPException
from bl.widow_bl import WidowBL
from injector import inject
from container import injector


router = APIRouter(tags=["Widows"])

@inject
def get_widow_bl() -> WidowBL:
    return injector.get(WidowBL)

@router.get("/widows/")
def get_all_widows(widow_bl: WidowBL = Depends(get_widow_bl)):
    return widow_bl.get_all_widows()

@router.get("/widows/{widow_id}")
def get_widow(widow_id: int, widow_bl: WidowBL = Depends(get_widow_bl)):
    widow = widow_bl.get_widow(widow_id)
    if not widow:
        raise HTTPException(status_code=404, detail="Widow not found")
    return widow

@router.get("/widows.rel/{widow_id}")
def get_widow_with_rel(widow_id: int, widow_bl: WidowBL = Depends(get_widow_bl)):
    widow = widow_bl.get_widow_with_rel(widow_id)
    if not widow:
        raise HTTPException(status_code=404, detail="Widow not found")
    return widow

@router.post("/widows/")
def create_widow(widow_data: dict, widow_bl: WidowBL = Depends(get_widow_bl)):
    return widow_bl.create_widow(widow_data)

@router.put("/widows/{widow_id}")
def update_widow(widow_id: int, widow_data: dict, widow_bl: WidowBL = Depends(get_widow_bl)):
    updated_widow = widow_bl.update_widow(widow_id, widow_data)
    if not updated_widow:
        raise HTTPException(status_code=404, detail="Widow not found")
    return updated_widow

@router.delete("/widows/{widow_id}")
def delete_widow(widow_id: int, widow_bl: WidowBL = Depends(get_widow_bl)):
    deleted_widow = widow_bl.delete_widow(widow_id)
    if not deleted_widow:
        raise HTTPException(status_code=404, detail="Widow not found")
    return {"detail": "Widow deleted successfully"}

@router.delete("/widows/")
def delete_all_widows(widow_bl: WidowBL = Depends(get_widow_bl)):
    widow_bl.delete_all_widows()
    return {"detail": "All widows deleted successfully"}
