import uuid

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import RedirectResponse

from . import repository, model, schema
from .database import SessionLocal, engine

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/shorten", response_model=schema.UrlCreateResponse)
async def create_shorten_url(
    url: schema.UrlCreateRequest, db: Session = Depends(get_db)
):
    create: schema.UrlCreate = schema.UrlCreate(
        url=url.url, short_url=str(uuid.uuid4())
    )
    db_url = repository.create_shorten_url(db, create)
    return schema.UrlCreateResponse(short_url=db_url.short_url)
