from storage import storage_manager

class book_manager():
    def __init__(self) -> None:
        self.storage_management = storage_manager()
        self.books = self.storage_management.get_books_from_store()

    def add_book(self, title, author, isbn):
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
        old_length = len(self.books)
        self.books = [book for book in self.books if book["isbn"] != isbn]
        if len(self.books) == old_length:
            return False
        else:
            self.storage_management.update_books_store(self.books)
            return True
        
    def search_book(self, title, author, isbn):
        book_found = False
        for book in self.books:
            if book["title"].lower() == title.lower() or book["author"].lower() == author.lower() or book["isbn"] == isbn:
                book_found = True
                print(book)
        if book_found:
            return True
        else:
            return False
        
    def list_books(self):
        for book in self.books:
            print(book)

    def list_available_books(self, checkout_management):
        checkedOutBooks = checkout_management.get_checkedOut_books()
        checkedOutBooksISBN = [book["isbn"] for book in checkedOutBooks]
        for book in self.books:
            if book["isbn"] not in checkedOutBooksISBN:
                print(book)

    def get_books(self):
        return self.books

