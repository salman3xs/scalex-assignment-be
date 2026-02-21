from fastapi import APIRouter

from app.views.auth_view import login

router = APIRouter(tags=["Authentication"])

router.add_api_route("/login", login, methods=["POST"])
