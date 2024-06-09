from fastapi import APIRouter, Path
from model import GuestBook
from datetime import datetime

gb_router = APIRouter()

gb_list = []
_counter = 0

@gb_router.post("/guestbook")
async def add_book(guestbook: GuestBook) -> dict:
    global _counter
    guestbook.id = _counter + 1
    _counter += 1
    gb_list.append(guestbook)
    return {
        "msg" : "todo successed"
    }

@gb_router.get("/guestbook")
async def retrieve_GuestBooks() -> dict:
    return {
        "books" : gb_list
    }

@gb_router.get("/guestbook/{gb_id}")
async def get_single_book(gb_id: int = Path(..., title = "ID")) -> dict:
    for gb in gb_list:
        if gb.id == gb_id:
            return {"book" : gb}
    return {"msg" : "There is no guestbook"}

@gb_router.delete("/guestbook/{gb_id}")
async def delete_book(gb_id: int = Path(..., title="ID")) -> dict:
    for index, book in enumerate(gb_list):
        if book.id == gb_id:
            del gb_list[index]
            return {"msg" : f"gb with ID {gb_id} deleted successfully"}
    return {"msg" : "gb with supplied ID doesn't exist"}