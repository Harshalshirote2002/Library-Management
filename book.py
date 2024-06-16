#!/usr/bin/env python3
"""
 * @file book.py
 * @author Harshal Shirote (harshalshirote2002@gmail.com)
 * @brief The book_manager class to Manager Books
 * @version 1.0.0
 * @date 2024-06-16
 *
 * @copyright Copyright (c) 2024
"""
from storage import storage_manager


class book_manager:
    def __init__(self) -> None:
        self.storage_management = storage_manager()
        self.books = self.storage_management.get_books_from_store()

    def add_book(self, title, author, isbn):
        """
        Adds book into books.json database

        Args:
            title (str): New Book's title
            author (str): New Book's author
            isbn (str): New Book's ISBN number

        Returns:
            None
        """
        book_exists = False
        for book in self.books:
            if book["isbn"] == isbn:
                book_exists = True
        if not book_exists:
            self.books.append({"title": title, "author": author, "isbn": isbn})
            self.storage_management.update_books_store(self.books)
            print("\nBook Added")
        else:
            print("\nBook ISBN is already taken")

    def delete_book(self, isbn):
        """
        Deletes book from books list

        Args:
            isbn (str): The Book's ISBN number

        Returns:
            Boolean
        """
        old_length = len(self.books)
        self.books = [book for book in self.books if book["isbn"] != isbn]
        if len(self.books) == old_length:
            return False
        else:
            self.storage_management.update_books_store(self.books)
            return True

    def search_book(self, title, author, isbn):
        """
        Searches book in all the books

        Args:
            title (str): The Book's title
            author (str): The Book's author
            isbn (str): The Book's ISBN number

        Returns:
            Boolean
        """
        book_found = False
        for book in self.books:
            if (
                book["title"].lower() == title.lower()
                or book["author"].lower() == author.lower()
                or book["isbn"] == isbn
            ):
                book_found = True
                print(book)
        if book_found:
            return True
        else:
            return False

    def list_books(self):
        """
        lists all books

        Args:
            None

        Returns:
            None
        """
        for book in self.books:
            print(book)

    def list_available_books(self, checkout_management):
        """
        Lists all the books available for check out

        Args:
            checkout_management (obj): The checkout management object

        Returns:
            None
        """
        checkedOutBooks = checkout_management.get_checkedOut_books()
        checkedOutBooksISBN = [book["isbn"] for book in checkedOutBooks]
        for book in self.books:
            if book["isbn"] not in checkedOutBooksISBN:
                print(book)

    def get_books(self):
        """
        returns all the books

        Args:
            None

        Returns:
            list
        """
        return self.books
