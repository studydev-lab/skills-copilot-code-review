"""
Announcement endpoints for the High School Management System API
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Dict, Any, Optional, List
from datetime import date
from bson import ObjectId

from ..database import announcements_collection, teachers_collection

router = APIRouter(
    prefix="/announcements",
    tags=["announcements"]
)


def _serialize_announcement(doc):
    """Convert a MongoDB document to a JSON-serializable dict."""
    doc["id"] = str(doc.pop("_id"))
    return doc


@router.get("", response_model=List[Dict[str, Any]])
def get_announcements() -> List[Dict[str, Any]]:
    """
    Get all active announcements.

    Returns announcements whose expiration_date has not passed and whose
    start_date (if set) is not in the future.
    """
    today = date.today().isoformat()
    query = {
        "expiration_date": {"$gte": today},
        "$or": [
            {"start_date": None},
            {"start_date": {"$lte": today}},
        ],
    }
    return [_serialize_announcement(doc) for doc in announcements_collection.find(query)]


@router.get("/all", response_model=List[Dict[str, Any]])
def get_all_announcements(teacher_username: str = Query(...)) -> List[Dict[str, Any]]:
    """
    Get all announcements (including expired) for management.
    Requires teacher authentication.
    """
    teacher = teachers_collection.find_one({"_id": teacher_username})
    if not teacher:
        raise HTTPException(status_code=401, detail="Authentication required")

    return [_serialize_announcement(doc) for doc in announcements_collection.find()]


@router.post("", response_model=Dict[str, Any])
def create_announcement(
    message: str = Query(...),
    expiration_date: str = Query(...),
    start_date: Optional[str] = Query(None),
    teacher_username: str = Query(...),
) -> Dict[str, Any]:
    """
    Create a new announcement. Requires teacher authentication.

    - message: The announcement text
    - expiration_date: When the announcement expires (YYYY-MM-DD)
    - start_date: Optional start date (YYYY-MM-DD)
    - teacher_username: The authenticated teacher's username
    """
    teacher = teachers_collection.find_one({"_id": teacher_username})
    if not teacher:
        raise HTTPException(status_code=401, detail="Authentication required")

    # Validate date formats
    try:
        date.fromisoformat(expiration_date)
        if start_date:
            date.fromisoformat(start_date)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")

    doc = {
        "message": message,
        "expiration_date": expiration_date,
        "start_date": start_date,
    }
    result = announcements_collection.insert_one(doc)
    return {"id": str(result.inserted_id), "message": message, "expiration_date": expiration_date, "start_date": start_date}


@router.put("/{announcement_id}", response_model=Dict[str, Any])
def update_announcement(
    announcement_id: str,
    message: str = Query(...),
    expiration_date: str = Query(...),
    start_date: Optional[str] = Query(None),
    teacher_username: str = Query(...),
) -> Dict[str, Any]:
    """
    Update an existing announcement. Requires teacher authentication.
    """
    teacher = teachers_collection.find_one({"_id": teacher_username})
    if not teacher:
        raise HTTPException(status_code=401, detail="Authentication required")

    try:
        date.fromisoformat(expiration_date)
        if start_date:
            date.fromisoformat(start_date)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")

    try:
        oid = ObjectId(announcement_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid announcement ID")

    result = announcements_collection.update_one(
        {"_id": oid},
        {"$set": {
            "message": message,
            "expiration_date": expiration_date,
            "start_date": start_date,
        }},
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Announcement not found")

    return {"id": announcement_id, "message": message, "expiration_date": expiration_date, "start_date": start_date}


@router.delete("/{announcement_id}")
def delete_announcement(
    announcement_id: str,
    teacher_username: str = Query(...),
) -> Dict[str, str]:
    """
    Delete an announcement. Requires teacher authentication.
    """
    teacher = teachers_collection.find_one({"_id": teacher_username})
    if not teacher:
        raise HTTPException(status_code=401, detail="Authentication required")

    try:
        oid = ObjectId(announcement_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid announcement ID")

    result = announcements_collection.delete_one({"_id": oid})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Announcement not found")

    return {"message": "Announcement deleted"}
