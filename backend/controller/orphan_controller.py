from fastapi import APIRouter, Depends, HTTPException
from injector import inject
from container import injector
from bl.orphan_bl import OrphanBL 

router = APIRouter(tags=["Orphans"])

@inject
def get_orphan_bl() -> OrphanBL:
    return injector.get(OrphanBL)

@router.get("/orphans/")
def get_all_orphans(orphan_bl: OrphanBL = Depends(get_orphan_bl)):
    return orphan_bl.get_all_orphans()

@router.get("/orphans/{orphan_id}")
def get_orphan(orphan_id: int, orphan_bl: OrphanBL = Depends(get_orphan_bl)):
    orphan = orphan_bl.get_orphan(orphan_id)
    if not orphan:
        raise HTTPException(status_code=404, detail="Orphan not found")
    return orphan

@router.get("/orphans.rel/{orphan_id}")
def get_orphan_with_rel(orphan_id: int, orphan_bl: OrphanBL = Depends(get_orphan_bl)):
    orphan = orphan_bl.get_orphan(orphan_id)
    if not orphan:
        raise HTTPException(status_code=404, detail="Orphan not found")
    return orphan

@router.post("/orphans/")
def create_orphan(orphan_data: dict, orphan_bl: OrphanBL = Depends(get_orphan_bl)):
    return orphan_bl.create_orphan(orphan_data)

@router.put("/orphans/{orphan_id}")
def update_orphan(orphan_id: int, orphan_data: dict, orphan_bl: OrphanBL = Depends(get_orphan_bl)):
    updated_orphan = orphan_bl.update_orphan(orphan_id, orphan_data)
    if not updated_orphan:
        raise HTTPException(status_code=404, detail="Orphan not found")
    return updated_orphan

@router.delete("/orphans/{orphan_id}")
def delete_orphan(orphan_id: int, orphan_bl: OrphanBL = Depends(get_orphan_bl)):
    deleted_orphan = orphan_bl.delete_orphan(orphan_id)
    if not deleted_orphan:
        raise HTTPException(status_code=404, detail="Orphan not found")
    return {"detail": "Orphan deleted successfully"}

@router.delete("/orphans/")
def delete_all_orphans(orphan_bl: OrphanBL = Depends(get_orphan_bl)):
    orphan_bl.delete_all_orphans()
    return {"detail": "All orphans deleted successfully"}
