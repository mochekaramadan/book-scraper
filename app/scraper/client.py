import asyncio
import httpx

class ScraperClient:
    def __init__(self, timeout: float = 10.0, retries: int = 3):
        self.timeout = timeout
        self.retries = retries

    async def fetch(self, url: str) -> str:
        for attempt in range(self.retries):
            try:
                async with httpx.AsyncClient(timeout=self.timeout) as client:
                    response = await client.get(url)
                    response.raise_for_status()
                    return response.text
            except httpx.HTTPError:
                if attempt == self.retries - 1:
                    raise
                await.asyncio.sleep(2 ** attempt)  # Exponential backoff
        raise RuntimeError("Failed to fetch URL after all retries")