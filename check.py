from storage import storage_manager

class check_manager():
    def __init__(self) -> None:
        self.storage_management = storage_manager()
        self.checkouts = self.storage_management.get_checkouts_from_store()

    def checkout_book(self, user_id, isbn):
        self.checkouts.append({"user_id": user_id, "isbn": isbn})
        self.storage_management.update_checkouts_store(self.checkouts)
