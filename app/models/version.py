from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.database.sql_connect import Base

class NoteVersion(Base):
    __tablename__ = "note_versions"
    id = Column(Integer, primary_key=True)
    note_id = Column(Integer, ForeignKey("notes.id", ondelete="CASCADE"), index=True, nullable=False)
    version = Column(Integer, nullable=False)
    content = Column(Text, nullable=False)
    editor_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    note = relationship("Note")
    editor = relationship("User")
