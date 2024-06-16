from storage import storage_manager

class user_manager():
    def __init__(self) -> None:
        self.storage_management = storage_manager()
        self.users = self.storage_management.get_users_from_store()

    def add_user(self, name, user_id):
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

    def delete_user(self, id):
        old_length = len(self.users)
        self.users = [user for user in self.users if user["user_ID"] != id]
        if len(self.users) == old_length:
            return False
        else:
            self.storage_management.update_users_store(self.users)
            return True
        
    def search_user(self, name, user_id):
        user_found = False
        for user in self.users:
            if user["name"].lower() == name.lower() or user["user_ID"]== user_id:
                user_found = True
                print(user)
        if user_found:
            return True
        else:
            return False
    
    def list_users(self):
        for user in self.users:
            print(user)

    def get_users(self):
        return self.users
