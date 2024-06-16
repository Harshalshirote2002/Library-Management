from storage import storage_manager
from check import check_manager

class book_manager():
    def __init__(self) -> None:
        self.storage_management = storage_manager()
        self.checkout_management = check_manager()
        self.books = self.storage_management.get_books_from_store()

    def add_book(self, title, author, isbn):
        self.books.append({"title": title, "author": author, "isbn": isbn})
        self.storage_management.update_books_store(self.books)

    def delete_book(self, isbn):
        old_length = len(self.books)
        self.books = [book for book in self.books if book["isbn"] != isbn]
        if len(self.books) == old_length:
            return False
        else:
            self.storage_management.update_books_store(self.books)
            return True
        
    def list_books(self):
        for book in self.books:
            print(book)

    def list_available_books(self):
        checkedOutBooks = self.checkout_management.get_checkedOut_books()
        checkedOutBooksISBN = [book["isbn"] for book in checkedOutBooks]
        for book in self.books:
            if book["isbn"] not in checkedOutBooksISBN:
                print(book)

