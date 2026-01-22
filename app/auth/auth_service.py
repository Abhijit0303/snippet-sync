from sqlalchemy.orm import Session

from app.auth.jwt import create_jwt_token
from app.auth.password import hash_password, verify_password
from app.models.user_model import User


class AuthService:

    @staticmethod
    def register(db: Session, email: str, password: str) -> User:
        hashed_password = hash_password(password)
        new_user = User(email=email, hashed_password=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    @staticmethod
    def authenticate(db: Session, email: str, password: str) -> User | None:
        user = db.query(User).filter(User.email == email).first()
        if user and verify_password(password, user.hashed_password):
            token = create_jwt_token({"sub": user.email})
            return token
        return None