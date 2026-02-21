from app.services.csv_service import csv_service


class BookController:
    """
    Controller handling book-related business logic.
    """

    def get_books(self, user_type: str) -> dict:
        """
        Gets books based on user type.
        Regular users see only regularUser.csv books.
        Admin users see books from both CSV files.

        Args:
            user_type: The type of user ("admin" or "regular").

        Returns:
            Dictionary with book data.
        """
        regular_books = csv_service.get_regular_books()

        if user_type == "admin":
            admin_books = csv_service.get_admin_books()
            return {
                "success": True,
                "user_type": user_type,
                "total_books": len(regular_books) + len(admin_books),
                "books": regular_books + admin_books,
            }

        return {
            "success": True,
            "user_type": user_type,
            "total_books": len(regular_books),
            "books": regular_books,
        }

    def add_book(self, book_name: str, author: str, publication_year: int) -> dict:
        """
        Adds a new book to regularUser.csv.

        Args:
            book_name: Name of the book.
            author: Author of the book.
            publication_year: Year of publication.

        Returns:
            Dictionary with success status and the newly added book.
        """
        new_book = csv_service.add_book(book_name, author, publication_year)
        return {
            "success": True,
            "message": "Book added successfully.",
            "book": new_book,
        }

    def delete_book(self, book_name: str) -> dict:
        """
        Deletes a book from regularUser.csv by name.

        Args:
            book_name: Name of the book to delete.

        Returns:
            Dictionary with success status and message.

        Raises:
            ValueError: If the book is not found.
        """
        deleted = csv_service.delete_book(book_name)

        if not deleted:
            raise ValueError(f'Book "{book_name}" not found in the library.')

        return {
            "success": True,
            "message": f'Book "{book_name}" deleted successfully.',
        }


book_controller = BookController()
