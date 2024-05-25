from sqlalchemy.orm import Session

from . import model, schema


def get_shorten_url_by_original_url(db: Session, shorten_url: str) -> model.Url:
    return db.query(model.Url).filter(model.Url.short_url == shorten_url).first()


def create_shorten_url(db: Session, url: schema.UrlCreate):
    db_url = model.Url(original_url=url.original_url, short_url=url.shorten_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url


def update_hits(db: Session, shorten_url: str):
    db.query(model.Url).filter(model.Url.short_url == shorten_url).update(
        {"hits": model.Url.hits + 1}
    )
    db.commit()
