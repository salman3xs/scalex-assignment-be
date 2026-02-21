from pydantic import BaseModel
from typing import Optional


class LoginRequest(BaseModel):
    """Request model for the /login endpoint."""
    username: str
    password: str


class LoginResponse(BaseModel):
    """Response model for a successful login."""
    success: bool
    message: str
    token: str
    user: dict
