from fastapi import HTTPException

from app.models.user_model import LoginRequest
from app.controllers.auth_controller import auth_controller


async def login(request: LoginRequest):
    """
    Authenticate a user and return a JWT token.

    - **username**: The username of the user
    - **password**: The password of the user

    Returns a JWT token on successful authentication.
    """
    try:
        result = auth_controller.login(request.username, request.password)
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail={"success": False, "message": str(e)},
        )
