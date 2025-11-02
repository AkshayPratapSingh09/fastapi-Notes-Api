from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.sql_connect import get_db
from app.schemas.version import VersionOut
from app.services.auth import get_current_user
from app.services.versions import list_versions, get_version, restore_version
from app.models.user import User
from app.schemas.note import NoteOut

router = APIRouter(prefix="/notes/{note_id}/versions", tags=["versions"])

@router.get("/", response_model=list[VersionOut])
def list_all(note_id: int, db: Session = Depends(get_db), current: User = Depends(get_current_user)):
    return list_versions(db, note_id, current.id)

@router.get("/{version}", response_model=VersionOut)
def one(note_id: int, version: int, db: Session = Depends(get_db), current: User = Depends(get_current_user)):
    return get_version(db, note_id, version, current.id)

@router.post("/{version}/restore", response_model=NoteOut)
def restore(note_id: int, version: int, db: Session = Depends(get_db), current: User = Depends(get_current_user)):
    return restore_version(db, note_id, version, current.id, current.id)
