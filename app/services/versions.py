from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.version import NoteVersion
from app.models.note import Note

def list_versions(db: Session, note_id: int, owner_id: int) -> list[NoteVersion]:
    owner_check = db.query(Note).filter(Note.id == note_id, Note.owner_id == owner_id).first()
    if not owner_check:
        raise HTTPException(status_code=404, detail="Note not found")
    return db.query(NoteVersion).filter(NoteVersion.note_id == note_id).order_by(NoteVersion.version.desc()).all()

def get_version(db: Session, note_id: int, version_num: int, owner_id: int) -> NoteVersion:
    owner_check = db.query(Note).filter(Note.id == note_id, Note.owner_id == owner_id).first()
    if not owner_check:
        raise HTTPException(status_code=404, detail="Note not found")
    v = db.query(NoteVersion).filter(NoteVersion.note_id == note_id, NoteVersion.version == version_num).first()
    if not v:
        raise HTTPException(status_code=404, detail="Version not found")
    return v

def restore_version(db: Session, note_id: int, version_num: int, owner_id: int, editor_id: int) -> Note:
    v = get_version(db, note_id, version_num, owner_id)
    note = db.query(Note).filter(Note.id == note_id, Note.owner_id == owner_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    note.content = v.content
    last = db.query(NoteVersion).filter(NoteVersion.note_id == note_id).order_by(NoteVersion.version.desc()).first()
    next_ver = (last.version + 1) if last else 1
    nv = NoteVersion(note_id=note_id, version=next_ver, content=note.content, editor_id=editor_id)
    db.add(nv)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note
