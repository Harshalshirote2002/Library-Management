from storage import storage_manager

class book_manager():
    def __init__(self) -> None:
        self.storage_management = storage_manager()
        self.books = self.storage_management.get_books_from_store()

    def add_book(self, title, author, isbn):
        self.books.append({"title": title, "author": author, "isbn": isbn})
        self.storage_management.update_books_store(self.books)

    def list_books(self):
        for book in self.books:
            print(book)

