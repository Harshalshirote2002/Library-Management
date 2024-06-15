from storage import storage_manager

class user_manager():
    def __init__(self) -> None:
        self.storage_management = storage_manager()
        self.users = self.storage_management.get_users_from_store()

    def add_user(self, name, user_id):
        self.users.append({"name": name, "user_ID": user_id})
        self.storage_management.update_users_store(self.users)

    def delete_user(self, id):
        old_length = len(self.users)
        self.users = [user for user in self.users if user["user_ID"] != id]
        if len(self.users) == old_length:
            return False
        else:
            self.storage_management.update_users_store(self.users)
            return True
    
    def list_users(self):
        for user in self.users:
            print(user)
