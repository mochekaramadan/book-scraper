from sqlaclchemy import select

from app.database import (
    BookDB,
    SessionLocal
)

from app.models.book import Book

def save_books(books: list[Book]) -> int:
    session = SessionLocal()
    created = 0
    try:
        for book in books:
            existing = session.scalar(
                select(BookDB).where(BookDB.url == book.url)
            )

            if existing:
                continue
            
            db_book = BookDB(
                title=book.title,
                price=book.price,
                availability=book.availability,
                url=book.url
                rating=book.rating
            )

            session.add(db_book)
            created += 1
        
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error saving books: {e}")
    finally:
        session.close()
    return created