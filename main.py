# This is a deliberately poorly implemented main script for a Library Management System.

from book import book_manager
from user import user_manager
from check import check_manager
import time

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Delete Book")
    print("3. List Books")
    print("4. Add User")
    print("5. Delete User")
    print("6. List Users")
    print("7. Checkout Book")
    print("8. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    book_management = book_manager()
    user_management = user_manager()
    checkout_management = check_manager()
    while True:
        choice = main_menu()
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book_management.add_book(title, author, isbn)
            print("Book added.")
        elif choice == '2':
            isbn = input("Enter ISBN: ")
            rem = book_management.delete_book(isbn)
            if rem:
                print("Book deleted.")
            else:
                print(f"Book with ISBN {isbn} not found!")
        elif choice == '3':
            book_management.list_books()
        elif choice == '4':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user_management.add_user(name, user_id)
            print("User added.")
        elif choice == '5':
            user_ID = input("Enter user ID: ")
            rem = user_management.delete_user(user_ID)
            if rem:
                print("User deleted.")
            else:
                print(f"User with ID {user_ID} not found!")
        elif choice == '6':
            user_management.list_users()
        elif choice == '7':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            checkout_management.checkout_book(user_id, isbn)
            print("Book checked out.")
        elif choice == '8':
            print("Exiting...")
            time.sleep(3)
            print("Thank You Visit Again!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
