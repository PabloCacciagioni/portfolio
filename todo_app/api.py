from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import engine, Base, get_db
from . import models

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root(db: Session = Depends(get_db)):
    return {"message": "Hello World"}



@app.get("/status")
async def get_status():
    return {"status": "ok"}
