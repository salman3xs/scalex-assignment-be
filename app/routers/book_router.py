from fastapi import APIRouter

from app.views.book_view import home, add_book, delete_book

router = APIRouter(tags=["Books"])

router.add_api_route("/home", home, methods=["GET"])
router.add_api_route("/addBook", add_book, methods=["POST"])
router.add_api_route("/deleteBook", delete_book, methods=["DELETE"])
