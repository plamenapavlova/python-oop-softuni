class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

class Library():
    def __init__(self, *args):
        self.books = list(args)

    def find_book(self, title):
        try:
            return [el for el in self.books if el.title == title][0]
        except IndexError:
            return "Book doesn't exist"

b1 = Book("Title", "Author")
b2 = Book("Title2", "Author2")
b3 = Book("Title3", "Author3")

lib = Library(b1, b2)
print(lib)
