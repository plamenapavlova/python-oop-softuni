from project.user import User


class Library:
    def __init__(self):
        self.user_records: list[User] = []
        self.books_available: dict = {}
        self.rented_books: dict = {}

    def get_book(self, author:str, book_name: str, days_to_return: int, user: User) -> str:
        if author in self.books_available and book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)
            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}
            self.rented_books[user.username][book_name] = days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        else:
            for username, books in self.rented_books.items():
                if book_name in books:
                    days_left = books[book_name]
                    return f'The book "{book_name}" is already rented and will be available in {days_left} days!'
            return None

    def return_book(self, author:str, book_name:str, user:User)-> str|None:
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"
        self.books_available.setdefault(author, []).append(book_name)
        if user.username in self.rented_books and book_name in self.rented_books[user.username]:
            del self.rented_books[user.username][book_name]
        user.books.remove(book_name)
        return None
