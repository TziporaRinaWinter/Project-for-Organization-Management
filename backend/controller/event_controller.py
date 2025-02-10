from fastapi import APIRouter, Depends, HTTPException
from injector import inject
from container import injector
from bl.event_bl import EventBL 

router = APIRouter(tags=["Events"])

@inject
def get_event_bl() -> EventBL:
    return injector.get(EventBL)

@router.get("/events/")
def get_all_events(event_bl: EventBL = Depends(get_event_bl)):
    return event_bl.get_all_events()

@router.get("/events/{event_id}")
def get_event(event_id: int, event_bl: EventBL = Depends(get_event_bl)):
    event = event_bl.get_event(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.get("/events.rel/{event_id}")
def get_event_with_rel(event_id: int, event_bl: EventBL = Depends(get_event_bl)):
    event = event_bl.get_event_with_rel(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.post("/events/")
def create_event(event_data: dict, event_bl: EventBL = Depends(get_event_bl)):
    return event_bl.create_event(event_data)

@router.put("/events/{event_id}")
def update_event(event_id: int, event_data: dict, event_bl: EventBL = Depends(get_event_bl)):
    updated_event = event_bl.update_event(event_id, event_data)
    if not updated_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated_event

@router.delete("/events/{event_id}")
def delete_event(event_id: int, event_bl: EventBL = Depends(get_event_bl)):
    deleted_event = event_bl.delete_event(event_id)
    if not deleted_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"detail": "Event deleted successfully"}

@router.delete("/events/")
def delete_all_events(event_bl: EventBL = Depends(get_event_bl)):
    event_bl.delete_all_events()
    return {"detail": "All events deleted successfully"}
