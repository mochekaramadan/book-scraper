from pydantic import BaseModel

class Book(BaseModel):
    title: str
    price: float
    availability: str
    rating: int
    url: str