import json
from datetime import datetime

class storage_manager():
    def __init__(self) -> None:
        self.__books_data_path = "database/books.json"
        self.__users_data_path = "database/users.json"
        self.__checkouts_data_path = "database/checkouts.json"

    def get_books_from_store(self) -> list:
        books = open(self.__books_data_path)
        books_data = json.load(books)
        return books_data["books"]
    
    def update_books_store(self, new_books_data):
        books_data = {
            "books": new_books_data,
            "last_updated": f"{datetime.now().strftime('%H:%M:%S %d-%m-%Y')}"
        }
        json_object = json.dumps(books_data, indent = 4)
        with open(self.__books_data_path, 'w') as file:
            file.write(json_object)

    def get_users_from_store(self) -> list:
        users = open(self.__users_data_path)
        users_data = json.load(users)
        return users_data["users"]
    
    def update_users_store(self, new_users_data):
        users_data = {
            "users": new_users_data,
            "last_updated": f"{datetime.now().strftime('%H:%M:%S %d-%m-%Y')}"
        }
        json_object = json.dumps(users_data, indent = 4)
        with open(self.__users_data_path, 'w') as file:
            file.write(json_object)

    def get_checkouts_from_store(self):
        checkouts = open(self.__checkouts_data_path)
        checkouts_data = json.load(checkouts)
        return checkouts_data["checkouts"]
    
    def update_checkouts_store(self, new_checkouts_data):
        checkouts_data = {
            "checkouts": new_checkouts_data,
            "last_updated": f"{datetime.now().strftime('%H:%M:%S %d-%m-%Y')}"
        }
        json_object = json.dumps(checkouts_data, indent=4)
        with open(self.__checkouts_data_path, 'w') as file:
            file.write(json_object)

    
if __name__ == "__main__":
    storage_management = storage_manager()
    print(storage_management.get_books_from_store())
    books = [{
        "title": "And then there were none",
        "author": "Agatha Christie",
        "isbn": "ISBN_99999"
    },
    {
        "title": "And then there were none",
        "author": "Agatha Christie",
        "isbn": "ISBN_99999"
    },
    {
        "title": "And then there were none",
        "author": "Agatha Christie",
        "isbn": "ISBN_99999"
    }]
    storage_management.update_books_store(books)
    obj1 = storage_management.get_books_from_store()
    print()
