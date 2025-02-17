class User:
    _users = []

    def __init__(self, ID, name, level='user'):
        self.ID = ID
        self.name = name
        self.level = level
        self._users.append(self)

    def view_user(self):
        print(f"User ID: {self.ID}, Name: {self.name}, Level: {self.level}")

    @classmethod
    def get_users(cls):
        return cls._users

class Admin(User):
    def __init__(self, ID, name, level='admin'):
        super().__init__(ID, name, level)
        self.__root = True

    def change_right(self):
        self.__root = not self.__root

    def add_user(self, ID, name, level='user'):
        if self.__root:
            new_user = User(ID, name, level)
            print(f"Пользователь {name} добавлен.")
            return new_user
        else:
            print(f"{self.name}: Недостаточно прав для добавления пользователя.")

    def remove_user(self, user):
        if user in self.__class__._users and self.__root:
            self.__class__._users.remove(user)
            print(f"Пользователь {user.name} удалён администратором.")
            del user
        else:
            print(f"{self.name}: Недостаточно прав для удаления пользователя.")

    def __del__(self):
        pass

# Пример использования
user1 = User(1, 'John')
user2 = User(5, 'Calvin')
admin1 = Admin(101, 'Jane')
admin2 = Admin(102, 'Jack')

user1.view_user()
admin1.view_user()
admin2.change_right()

# Администратор добавляет нового пользователя
new_user = admin1.add_user(3, 'Alice')
new_user.view_user()
admin1.add_user(7, 'Donald', 'guest')

# Администратор удаляет пользователя
admin1.remove_user(user1)

# Попытка удаления пользователя администратором без прав
admin2.remove_user(user2)

# Вывод всех пользователей
for user in User.get_users():
    user.view_user()

# Попытка доступа к удаленному пользователю вызовет ошибку
try:
    print(user1.name, user1.level)
except NameError as e:
    print(f"Ошибка: {e}")
