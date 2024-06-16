from storage import storage_manager

class check_manager():
    def __init__(self) -> None:
        self.storage_management = storage_manager()
        self.checkouts = self.storage_management.get_checkouts_from_store()

    def checkout_book(self, user_id, isbn):
        self.checkouts.append({"user_id": user_id, "isbn": isbn})
        self.storage_management.update_checkouts_store(self.checkouts)

    def checkIn_book(self, user_id, isbn):
        new_checkouts = [checkout for checkout in self.checkouts if checkout["user_ID"] != user_id and checkout["isbn"] != isbn]
        for checkout in new_checkouts:
            print(checkout)

    def get_checkedOut_books(self):
        return self.checkouts
