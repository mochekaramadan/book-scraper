import asyncio

from app.scraper.client import ScraperClient
from app.scraper.parser import parse_books
from app.database.database import init_db
from app.service.book_service import save_books

URL = "https://books.toscrape.com/"
semaphore = asyncio.Semaphore(5)


def get_page_url(page_number: int) -> str:
    if page_number == 1:
        return URL
    return f"{URL}catalogue/page-{page_number}.html"

async def scrape_pages(start_page: int, end_page: int):
    client = ScraperClient()
    tasks = [
        scrape_page(client, page)
        for page in range (start_page, end_page + 1)
    ]
    results = await asyncio.gather(*tasks)
    books = []
    for page_books in results:
        books.extend(page_books)
    return books

async def scrape_page(client: ScraperClient, page: int):
    async with semaphore:
        url = get_page_url(page)
        print(f"Scraping page {page}: {url}")
        html = await client.fetch(url)
        books = parse_books(html)
        return books

async def main():
    init_db()


    books = await scrape_pages(1, 5)
    print(f"Found {len(books)} books")
    saved = save_books(books)
    print(f"Saved {saved} books")

if __name__ == "__main__":
    asyncio.run(main())

