from fastapi import APIRouter, Depends

from authMain import get_current_user_db
from models.user import User
from models.chats import Chat
from schemas.chat_schema import ChatRequest
from database import get_db

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

# getting api key

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

router = APIRouter(prefix="/chat", tags=["chat"])

# chat endpoint which is protected with get_current_user_db
@router.post("/chat")
async def chat(requestmodel: ChatRequest, user: User = Depends(get_current_user_db), db: AsyncSession = Depends(get_db)):

    # handling the response
    try:
        response = client.models.generate_content(
        model= "gemini-2.5-flash",
        contents= f"""
        You are a simple AI tutor.

        Rules:
        - Give short answers.
        - Maximum 2-4 lines.
        - Use simple English.

        Question: {requestmodel.prompt}
"""
)

        ai_response = response.text


        if not ai_response:
            return {
                "error": "Gemini returned no response."
            }
        
        # adding prompt + response to db

        chat_entry = Chat(
            user_id=user.id,
            prompt=requestmodel.prompt,
            response=ai_response
        )

        db.add(chat_entry)

        await db.commit()
        await db.refresh(chat_entry)

        return {
            "response": ai_response
        }

    except Exception as e:
        return {
            "error": str(e)
        }


@router.get("/history")
async def history(db: AsyncSession = Depends(get_db), user: User = Depends(get_current_user_db)):
    result = await db.execute(
        select(Chat).where(
            Chat.user_id == user.id
        )
    )

    chats = result.scalars().all()

    return chats