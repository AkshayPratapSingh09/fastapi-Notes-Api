from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.sql_connect import get_db
from app.schemas.user import UserOut
from app.services.auth import get_current_user
from app.models.user import User

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserOut)
def me(db: Session = Depends(get_db), current: User = Depends(get_current_user)):
    return current
