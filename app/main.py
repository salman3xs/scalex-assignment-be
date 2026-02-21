import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.utils import get_openapi

from app.routers.auth_router import router as auth_router
from app.routers.book_router import router as book_router
from app.middleware.jwt_middleware import JWTMiddleware
from app.helper.validation_handler import validation_exception_handler

app = FastAPI(
    title="Library Management API",
    description="A FastAPI application for managing a library of books with JWT authentication and role-based access control.",
    version="1.0.0",
    swagger_ui_parameters={"persistAuthorization": True},
)

app.add_exception_handler(RequestValidationError, validation_exception_handler)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    openapi_schema["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

# --- Middleware ---
app.add_middleware(JWTMiddleware)

# --- Register Routers ---
app.include_router(auth_router)
app.include_router(book_router)


async def health_check():
    return {
        "success": True,
        "message": "Library API is running.",
        "endpoints": {
            "login": "POST /login",
            "home": "GET /home (requires JWT)",
            "addBook": "POST /addBook (requires JWT + admin)",
            "deleteBook": "DELETE /deleteBook (requires JWT + admin)",
            "docs": "GET /docs (Swagger UI)",
        },
    }

app.add_api_route("/", health_check, methods=["GET"], tags=["Health"])


if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT = 8000
    uvicorn.run("app.main:app", host=HOST, port=PORT, reload=True)
