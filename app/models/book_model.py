from pydantic import BaseModel, Field
from datetime import datetime


class AddBookRequest(BaseModel):
    """Request model for the /addBook endpoint."""
    bookName: str = Field(..., min_length=1, description="Name of the book")
    author: str = Field(..., min_length=1, description="Author of the book")
    publicationYear: int = Field(
        ...,
        ge=1,
        le=datetime.now().year,
        description="Year of publication (must be a valid year)",
    )


class DeleteBookRequest(BaseModel):
    """Request model for the /deleteBook endpoint."""
    bookName: str = Field(..., min_length=1, description="Name of the book to delete")


class BookResponse(BaseModel):
    """Model representing a single book record."""
    book_name: str
    author: str
    publication_year: str
