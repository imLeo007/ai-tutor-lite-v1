from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# postgreSQL Engine

engine = create_async_engine(
    DATABASE_URL
)

# Session Factory

SessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Base class for models

Base = declarative_base()

# Dependency

async def get_db():

    async with SessionLocal() as db:
        yield db