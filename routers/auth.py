from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy import select

from models.user import User

from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db

from authMain import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

# signup endpoint

@router.post("/signup")
async def signup(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(User).where(
            User.username == form_data.username
        )
    )

    existing_user = result.scalar_one_or_none()

    # checking if the username is already exists

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already Exists")
            
    # if it's a new one hash the password insert into the table
    
    hashed = hash_password(form_data.password)

    user = User(
        username=form_data.username,
        password=hashed
    )

    db.add(user)

    await db.commit()

    await db.refresh(user)

    return {"message": "User account created"}

# login endpoint

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):

    result = await db.execute(
        select(User).where(
            User.username == form_data.username
        )
    )

    user = result.scalar_one_or_none()

    # checking if the username and password is matching

    if not user:
        raise HTTPException(status_code=401, detail="Invalid Username")

    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid Password")
            
    # creating a token
            
    token = create_access_token({
        "username": form_data.username
        })

    return {
    "access_token": token,
    "token_type": "bearer"
    }