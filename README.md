# Book Scraper API

A Python web scraping project that collects book information from
Books to Scrape and exposes the collected data through a REST API.

## Features

- Async HTTP scraping
- HTML parsing with BeautifulSoup
- Pagination
- Retry with exponential backoff
- Concurrency control
- Data validation with Pydantic
- SQLite persistence
- Duplicate prevention
- REST API with FastAPI
- Search and filtering
- API pagination
- Unit testing
- Integration testing

## Tech Stack

- Python
- HTTPX
- BeautifulSoup
- Pydantic
- SQLAlchemy
- SQLite
- FastAPI
- Pytest

## Installation

```bash
git clone <repository-url>

cd book-scraper

python -m venv .venv