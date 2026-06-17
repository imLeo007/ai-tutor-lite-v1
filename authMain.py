from datetime import datetime, timedelta, timezone

from database import get_db

from sqlalchemy import select

from models.user import User

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import HTTPException, Depends

from fastapi.security import OAuth2PasswordBearer

from jose import jwt, JWTError

from passlib.context import CryptContext

import os

from dotenv import load_dotenv

load_dotenv()

# Secret key

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

# hashing instance

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# token reader from auth header where login endpoint is

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# hashing password

def hash_password(password:str):
    return pwd_context.hash(password)

# verifying password

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# creating a token from using data {"username": username}

def create_access_token(data: dict):

    # copying the data

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=30)

    # adding expiry time

    to_encode.update(
        {
            "exp": expire
        }
    )

    # creating a token

    token = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm="HS256")

    return token

# getting current user with token as oauth2_scheme gets it from auth header

def get_current_user(token:str = Depends(oauth2_scheme)):

    # JWT will throw an exception if there is no username

    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])

        # getting the username from the token

        username = payload.get("username")

        # if the username is not present throw an exception

        if username is None:
            raise HTTPException(status_code=401,detail="Invlid Token")
        
        return username
    
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


# getting the current user db with using current_user_db a protected endpoint as a dependency injection

async def get_current_user_db(db: AsyncSession = Depends(get_db)  ,username: str = Depends(get_current_user)):
    result = await db.execute(select(User).where(
        User.username == username
    ))

    user = result.scalar_one_or_none()

    return user