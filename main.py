class User():
    def __init__(self,ID, name):
        self._ID = ID
        self._name = name
        self._access_level = "user"

    def get_ID(self):
        return self._ID

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, new_name):
        self._name = new_name
        print({new_name})

class Admin(User):
    def __init__(self,ID, name):
        super().__init__(ID, name)
        self._access_level = "admin"
    def add_user(self,user_list, user):
        user_list.append(user)
        print(f"Пользователь добавлен")
        print(user_list)

    def remove_user(self,user_list, user):
        user_list.remove(user)
        print(f"Пользователь удален")
        print(user_list)

users = []
admin = Admin("6565", "Artem")
user1 = User("233", "Sasha")
user2 = User("123", "Pasha")
user3 = User("456", "Dima")

print(user1.get_name())
user2.set_name("Petr")
admin.add_user(users,user1)
admin.add_user(users,user3)
admin.add_user(users,user2)
admin.remove_user(users, user3)
