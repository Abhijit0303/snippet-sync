
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.auth.jwt import verify_jwt_token
from app.auth.token_blacklist import is_token_blacklisted


oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_schema)):
    if is_token_blacklisted(token):
        raise HTTPException(status_code=401, detail="Token has been revoked")

    payload = verify_jwt_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return payload["sub"]
