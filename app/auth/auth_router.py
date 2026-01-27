from fastapi import APIRouter, Depends, HTTPException, Header, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth.auth_service import AuthService
from app.auth.dependency import get_current_user
from app.database import get_db
from app.models.user_model import User
from app.schemas.auth_schema import UserCreateSchema
from app.auth.token_blacklist import blacklist_token

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

@router.get("/me")
def read_current_user(current_user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == current_user).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.post("/logout")
def logout(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization header",
        )

    token = authorization.split(" ")[1]
    blacklist_token(token)

    return {"message": "Successfully logged out"}