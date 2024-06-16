#!/usr/bin/env python3
"""
 * @file user.py
 * @author Harshal Shirote (harshalshirote2002@gmail.com)
 * @brief The user_manager class to Manager Users
 * @version 1.0.0
 * @date 2024-06-16
 *
 * @copyright Copyright (c) 2024
"""
from storage import storage_manager


class user_manager:
    def __init__(self) -> None:
        self.storage_management = storage_manager()
        self.users = self.storage_management.get_users_from_store()

    def add_user(self, name, user_id):
        """
        Adds user into users.json database

        Args:
            name (str): New User's name
            user_id (str): New User's unique ID

        Returns:
            None
        """
        user_exists = False
        for user in self.users:
            if user["user_ID"] == user_id:
                user_exists = True
        if not user_exists:
            self.users.append({"name": name, "user_ID": user_id})
            self.storage_management.update_users_store(self.users)
            print("\nUser Added")
        else:
            print("\nUser ID is taken. please choose another")

    def delete_user(self, user_id):
        """
        Deletes the user from users list

        Args:
            user_id (str): The User's unique ID

        Returns:
            Boolean
        """
        old_length = len(self.users)
        self.users = [user for user in self.users if user["user_ID"] != user_id]
        if len(self.users) == old_length:
            return False
        else:
            self.storage_management.update_users_store(self.users)
            return True

    def search_user(self, name, user_id):
        """
        Searches user in users list

        Args:
            name (str): The User's name
            user_id (str): The User's unique ID

        Returns:
            Boolean
        """
        user_found = False
        for user in self.users:
            if user["name"].lower() == name.lower() or user["user_ID"] == user_id:
                user_found = True
                print(user)
        if user_found:
            return True
        else:
            return False

    def list_users(self):
        """
        Lists all the users

        Args:
            None

        Returns:
            None
        """
        for user in self.users:
            print(user)

    def get_users(self):
        """
        returns all users

        Args:
            None

        Returns:
            list
        """
        return self.users
