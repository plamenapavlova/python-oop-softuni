from project import user
from project.library import Library
from project.user import User


class Registration:
    def add_user(self, user:User, library:Library) -> str|None:
        for u in library.user_records:
            if u.user_id == user.user_id:
                return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)
        return None

    def remove_user(self, user:User, library: Library)-> None|str:
        for u in library.user_records:
            if u.user_id == user.user_id:
                library.user_records.remove(u)
                return None
        return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library)-> str:
        for u in library.user_records:
            if user_id == u.user_id:
                if u.username == new_username:
                    return ("Please check again the provided username - it should be different than the username "
                            "used so far!")
                old_username = u.username
                u.username = new_username
                if old_username in library.rented_books:
                    library.rented_books[new_username] = library.rented_books.pop(old_username)
                return f"Username successfully changed to: {new_username} for user id: {user_id}"

        return f"There is no user with id = {user_id}!"

