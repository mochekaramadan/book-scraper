from fastapi import FastAPI, Query
from sqlalchemy import select

from app.database.database import (
    BookDB,
    SessionLocal,
    init_db,
)

app = FastAPI(
    title="Book Scraper API",
    version="1.0.0"
)

@app.on_event("startup")
def startup():
    init_db()


@app.get("/books")
def get_books(
    search: str | None = None,
    rating: int | None = None,
    page: int = Query(
        default=1,
        ge=1,
    ),
    limit: int = Query(
        default=10,
        ge=1,
        le=100,
    ),
):
    session = SessionLocal()
    try:
        query = select(BookDB)
        if search:
            query = query.where(BookDB.title.ilike(f"%{search}%"))
        if rating:
            query = query.where(BookDB.rating == rating)
        offset = (page - 1) * limit
        query = query.offset(offset).limit(limit)
        books = session.execute(query).scalars().all()
        return books
    except Exception as e:
        return {"error": str(e)}
    finally:
        session.close()