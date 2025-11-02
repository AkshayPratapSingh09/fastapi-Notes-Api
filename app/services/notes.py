from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.note import Note
from app.models.version import NoteVersion

def create_note(db: Session, owner_id: int, title: str, content: str) -> Note:
    note = Note(title=title, content=content, owner_id=owner_id)
    db.add(note)
    db.commit()
    db.refresh(note)
    version = NoteVersion(note_id=note.id, version=1, content=content, editor_id=owner_id)
    db.add(version)
    db.commit()
    return note

def get_note(db: Session, note_id: int, owner_id: int) -> Note:
    note = db.query(Note).filter(Note.id == note_id, Note.owner_id == owner_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

def list_notes(db: Session, owner_id: int) -> list[Note]:
    return db.query(Note).filter(Note.owner_id == owner_id).order_by(Note.updated_at.desc()).all()

def update_note(db: Session, note_id: int, owner_id: int, title: str | None, content: str | None, editor_id: int) -> Note:
    note = get_note(db, note_id, owner_id)
    if title is None and content is None:
        return note
    if title is not None:
        note.title = title
    if content is not None:
        note.content = content
        last_version = db.query(NoteVersion).filter(NoteVersion.note_id == note.id).order_by(NoteVersion.version.desc()).first()
        next_version = (last_version.version + 1) if last_version else 1
        v = NoteVersion(note_id=note.id, version=next_version, content=note.content, editor_id=editor_id)
        db.add(v)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

def delete_note(db: Session, note_id: int, owner_id: int) -> None:
    note = get_note(db, note_id, owner_id)
    db.delete(note)
    db.commit()
