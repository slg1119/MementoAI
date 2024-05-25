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


@app.get("/{shorten_url}", response_class=RedirectResponse, status_code=301)
async def redirect(shorten_url: str, db: Session = Depends(get_db)):
    model_url: model.Url = repository.get_shorten_url_by_original_url(db, shorten_url)
    if not model_url:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="데이터를 찾을 수 없습니다."
        )
    repository.update_hits(db, shorten_url)
    return model_url.original_url


@app.get("/stats/{shorten_url}", response_model=schema.UrlStats)
async def get_stats(shorten_url: str, db: Session = Depends(get_db)):
    model_url: model.Url = repository.get_shorten_url_by_original_url(db, shorten_url)
    if not model_url:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="데이터를 찾을 수 없습니다."
        )
    return schema.UrlStats(short_url=model_url.short_url, hits=model_url.hits)
