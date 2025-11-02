from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.database.sql_connect import get_db
from app.schemas.user import UserCreate, UserOut
from app.schemas.auth import Token
from app.services.users import create_user
from app.services.auth import create_access_token, authenticate

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.email, user.password)

@router.post("/login", response_model=Token)
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate(db, form.username, form.password)
    token = create_access_token({"sub": str(user.id)})
    return Token(access_token=token)
