from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.sql_connect import get_db
from app.schemas.note import NoteCreate, NoteUpdate, NoteOut
from app.services.auth import get_current_user
from app.services.notes import create_note, list_notes, get_note, update_note, delete_note
from app.models.user import User

router = APIRouter(prefix="/notes", tags=["notes"])

@router.post("/", response_model=NoteOut, status_code=status.HTTP_201_CREATED)
def create(payload: NoteCreate, db: Session = Depends(get_db), current: User = Depends(get_current_user)):
    return create_note(db, current.id, payload.title, payload.content)

@router.get("/", response_model=list[NoteOut])
def all(db: Session = Depends(get_db), current: User = Depends(get_current_user)):
    return list_notes(db, current.id)

@router.get("/{note_id}", response_model=NoteOut)
def one(note_id: int, db: Session = Depends(get_db), current: User = Depends(get_current_user)):
    return get_note(db, note_id, current.id)

@router.patch("/{note_id}", response_model=NoteOut)
def update(note_id: int, payload: NoteUpdate, db: Session = Depends(get_db), current: User = Depends(get_current_user)):
    return update_note(db, note_id, current.id, payload.title, payload.content, current.id)

@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(note_id: int, db: Session = Depends(get_db), current: User = Depends(get_current_user)):
    delete_note(db, note_id, current.id)
    return
