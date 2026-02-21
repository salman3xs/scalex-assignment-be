import csv
from pathlib import Path
from typing import List

from app.config.constant import REGULAR_CSV_PATH, ADMIN_CSV_PATH


class CSVService:
    """
    Service for reading and writing CSV book data files.
    """

    def read_csv(self, file_path: Path) -> List[dict]:
        """
        Reads a CSV file and returns a list of book dictionaries.

        Args:
            file_path: Path to the CSV file.

        Returns:
            List of dictionaries, each representing a book row.
        """
        books = []
        with open(file_path, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                books.append(dict(row))
        return books

    def write_csv(self, file_path: Path, books: List[dict]) -> None:
        """
        Writes a list of book dictionaries to a CSV file (overwrites).

        Args:
            file_path: Path to the CSV file.
            books: List of book dictionaries to write.
        """
        fieldnames = ["Book Name", "Author", "Publication Year"]
        with open(file_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(books)

    def get_regular_books(self) -> List[dict]:
        """Reads books from regularUser.csv."""
        return self.read_csv(REGULAR_CSV_PATH)

    def get_admin_books(self) -> List[dict]:
        """Reads books from adminUser.csv."""
        return self.read_csv(ADMIN_CSV_PATH)

    def add_book(self, book_name: str, author: str, publication_year: int) -> dict:
        """
        Adds a new book to regularUser.csv.

        Args:
            book_name: Name of the book.
            author: Author of the book.
            publication_year: Year of publication.

        Returns:
            Dictionary of the newly added book.
        """
        books = self.read_csv(REGULAR_CSV_PATH)
        new_book = {
            "Book Name": book_name,
            "Author": author,
            "Publication Year": str(publication_year),
        }
        books.append(new_book)
        self.write_csv(REGULAR_CSV_PATH, books)
        return new_book

    def delete_book(self, book_name: str) -> bool:
        """
        Deletes a book from regularUser.csv (case-insensitive match).

        Args:
            book_name: Name of the book to delete.

        Returns:
            True if the book was found and deleted, False otherwise.
        """
        books = self.read_csv(REGULAR_CSV_PATH)
        filtered_books = [
            book
            for book in books
            if book["Book Name"].strip().lower() != book_name.strip().lower()
        ]

        if len(filtered_books) == len(books):
            return False

        self.write_csv(REGULAR_CSV_PATH, filtered_books)
        return True


csv_service = CSVService()
