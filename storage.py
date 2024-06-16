#!/usr/bin/env python3
"""
 * @file storage.py
 * @author Harshal Shirote (harshalshirote2002@gmail.com)
 * @brief The storage_manager class to Manage json file storage
 * @version 1.0.0
 * @date 2024-06-16
 *
 * @copyright Copyright (c) 2024
"""
import json
from datetime import datetime


class storage_manager:
    def __init__(self) -> None:
        self.__books_data_path = "database/books.json"
        self.__users_data_path = "database/users.json"
        self.__checkouts_data_path = "database/checkouts.json"

    def get_books_from_store(self) -> list:
        """
        Returns books from books.json database

        Args:
            None

        Returns:
            List
        """
        books = open(self.__books_data_path)
        books_data = json.load(books)
        return books_data["books"]

    def update_books_store(self, new_books_data):
        """
        Updates books.json database

        Args:
            new_books_data (list): New list of books to be stored

        Returns:
            None
        """
        books_data = {
            "books": new_books_data,
            "last_updated": f"{datetime.now().strftime('%H:%M:%S %d-%m-%Y')}",
        }
        json_object = json.dumps(books_data, indent=4)
        with open(self.__books_data_path, "w") as file:
            file.write(json_object)

    def get_users_from_store(self) -> list:
        """
        Returns users from users.json database

        Args:
            None

        Returns:
            List
        """
        users = open(self.__users_data_path)
        users_data = json.load(users)
        return users_data["users"]

    def update_users_store(self, new_users_data):
        """
        Updates users.json database

        Args:
            new_users_data (str): New list of users to be stored

        Returns:
            None
        """
        users_data = {
            "users": new_users_data,
            "last_updated": f"{datetime.now().strftime('%H:%M:%S %d-%m-%Y')}",
        }
        json_object = json.dumps(users_data, indent=4)
        with open(self.__users_data_path, "w") as file:
            file.write(json_object)

    def get_checkouts_from_store(self):
        """
        Returns checkouts from checkouts.json database

        Args:
            None

        Returns:
            List
        """
        checkouts = open(self.__checkouts_data_path)
        checkouts_data = json.load(checkouts)
        return checkouts_data["checkouts"]

    def update_checkouts_store(self, new_checkouts_data):
        """
        Updates checkouts.json database

        Args:
            new_checkouts_data (str): New list of checkouts to be stored

        Returns:
            None
        """
        checkouts_data = {
            "checkouts": new_checkouts_data,
            "last_updated": f"{datetime.now().strftime('%H:%M:%S %d-%m-%Y')}",
        }
        json_object = json.dumps(checkouts_data, indent=4)
        with open(self.__checkouts_data_path, "w") as file:
            file.write(json_object)


if __name__ == "__main__":
    pass
