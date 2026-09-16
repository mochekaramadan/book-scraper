from urllib.parse import urljoin
from bs4 import BeautifulSoup
from app.models.book import Book

BASE_URL = "http://books.toscrape.com/"

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

def parse_books(html: str) -> list[Book]:
    soup = BeautifulSoup(html, "html.parser")
    books = []

    for article in soup.select(
        "article.product_pod"
    ):
        title_element = article.select_one("h3 a")
        price_element = article.select_one(".price_color")
        availability_element = article.select_one(".availability")
        rating_element = article.select_one(".star-rating")

        title = title_element.get("title", "").strip()
        price_text = price_element.get_text(strip=True)
        price = float(price_text.replace("£", ""))
        availability = availability_element.get_text("", strip=True)
        rating_class = rating_element.get("class", [])
        rating = 0

        for class_name in rating_class:
            if class_name in RATING_MAP:
                rating = RATING_MAP[class_name]
        
        relative_url = title_element.get("href")

        url = urljoin(BASE_URL, relative_url)

        books.append(
            Book(
                title=title,
                price=price,
                availability=availability,
                rating=rating,
                url=url
            )
        )

    return books