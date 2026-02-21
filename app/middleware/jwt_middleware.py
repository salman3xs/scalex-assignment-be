from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.utils.jwt_handler import jwt_handler

# Paths that don't require JWT authentication
EXCLUDED_PATHS = ["/login", "/", "/docs", "/openapi.json", "/redoc"]


class JWTMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        # Skip JWT check for excluded paths
        if request.url.path in EXCLUDED_PATHS:
            return await call_next(request)

        # Extract Authorization header
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse(
                status_code=401,
                content={
                    "success": False,
                    "message": "Access denied. No token provided.",
                },
            )

        token = auth_header.split(" ")[1]
        payload = jwt_handler.verify_token(token)

        if payload is None:
            return JSONResponse(
                status_code=401,
                content={
                    "success": False,
                    "message": "Invalid or expired token.",
                },
            )

        # Attach user info to request state
        request.state.user = payload
        return await call_next(request)
