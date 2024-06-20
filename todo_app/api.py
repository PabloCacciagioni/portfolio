from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from .database import get_session, init_db
from .models import Todo
import asyncio

app = FastAPI()

@app.post("/todos/", response_model=Todo)
async def create_todo(todo: Todo, session: AsyncSession = Depends(get_session)):
    session.add(todo)
    await session.commit()
    await session.refresh(todo)
    return todo

@app.get("/todos/", response_model=List[Todo])
async def read_todos(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Todo))
    todos = result.scalars().all()
    return todos 

async def startup():
    loop = asyncio.get_event_loop()
    await init_db()
    
app.add_event_handler("startup", startup)