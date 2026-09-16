import asyncio

from app.scraper.client import ScraperClient
from app.scraper.parser import parse_books

URL = "https://books.toscrape.com/"

async def main():

    client = ScraperClient()
    html = await client.fetch(URL)
    books = parse_books(html)

    print(f"Found {len(books)} books")

    for book in books:
        print(f"Title: {book.title}")
        print(f"Price: £{book.price}")
        print(f"Availability: {book.availability}")
        print(f"Rating: {book.rating} stars")
        print(f"URL: {book.url}")
        print("-" * 40)

if __name__ == "__main__":
    asyncio.run(main())