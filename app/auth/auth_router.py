from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth.auth_service import AuthService
from app.database import get_db
from app.models.user_model import User
from app.schemas.auth_schema import TokenSchema, UserCreateSchema

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register(data: UserCreateSchema, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == data.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    return AuthService.register(db, data.email, data.password)

@router.post("/login")
def login(from_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    token = AuthService.authenticate(db, from_data.username, from_data.password)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}