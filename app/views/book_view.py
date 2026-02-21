from fastapi import HTTPException, Request

from app.models.book_model import AddBookRequest, DeleteBookRequest
from app.controllers.book_controller import book_controller


async def home(request: Request):
    try:
        current_user = request.state.user
        result = book_controller.get_books(current_user["user_type"])
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"success": False, "message": "Error reading book data.", "error": str(e)},
        )


async def add_book(request: Request, body: AddBookRequest):
    current_user = request.state.user

    if current_user["user_type"] != "admin":
        raise HTTPException(
            status_code=403,
            detail={"success": False, "message": "Access denied. Admin privileges required."},
        )

    try:
        result = book_controller.add_book(
            body.bookName, body.author, body.publicationYear
        )
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"success": False, "message": "Error adding book.", "error": str(e)},
        )


async def delete_book(request: Request, body: DeleteBookRequest):
    current_user = request.state.user

    if current_user["user_type"] != "admin":
        raise HTTPException(
            status_code=403,
            detail={"success": False, "message": "Access denied. Admin privileges required."},
        )

    try:
        result = book_controller.delete_book(body.bookName)
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail={"success": False, "message": str(e)},
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"success": False, "message": "Error deleting book.", "error": str(e)},
        )
