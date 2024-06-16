#!/usr/bin/env python3
"""
 * @file check.py
 * @author Harshal Shirote (harshalshirote2002@gmail.com)
 * @brief The check_manager class to Manage checkIns and checkOuts
 * @version 1.0.0
 * @date 2024-06-16
 *
 * @copyright Copyright (c) 2024
"""
from storage import storage_manager


class check_manager:
    def __init__(self) -> None:
        self.storage_management = storage_manager()
        self.checkouts = self.storage_management.get_checkouts_from_store()

    def checkout_book(self, user_id, isbn, user_management, book_management):
        """
        Adds checkout to checkouts.json database

        Args:
            user_id (str): The user's unique ID
            isbn (str): The book's ISBN number
            user_management (obj): The user management object
            book_management (obj): The book management object

        Returns:
            None
        """
        users = user_management.get_users()
        books = book_management.get_books()
        user_exists = False
        book_exists = False
        book_checkedOut = False
        for user in users:
            if user["user_ID"] == user_id:
                user_exists = True
        for book in books:
            if book["isbn"] == isbn:
                book_exists = True
        if not user_exists:
            print(f"\nUser with ID {user_id} does not exist")
            return
        if not book_exists:
            print(f"\nBook with ISBN {isbn} does not exist")
            return
        for checkout in self.checkouts:
            if checkout["isbn"] == isbn:
                book_checkedOut = True
        if not book_checkedOut:
            self.checkouts.append({"user_ID": user_id, "isbn": isbn})
            self.storage_management.update_checkouts_store(self.checkouts)
            print("\nBook Checked Out")
        else:
            print("\nBook already Checked Out")

    def checkIn_book(self, user_id, isbn):
        """
        Removes checkout from checkouts.json database

        Args:
            user_id (str): The user's unique ID
            isbn (str): The book's ISBN number

        Returns:
            Boolean
        """
        new_checkouts = [
            checkout
            for checkout in self.checkouts
            if (checkout["user_ID"] != user_id or checkout["isbn"] != isbn)
        ]
        if len(new_checkouts) == len(self.checkouts):
            return False
        else:
            self.checkouts = new_checkouts
            self.storage_management.update_checkouts_store(new_checkouts)
            return True

    def get_checkedOut_books(self):
        """
        returns checkouts

        Args:
            None

        Returns:
            list
        """
        return self.checkouts
