from pydantic import BaseModel

class GuestBook(BaseModel):
    id: int
    title: str
    body: str
    time: str