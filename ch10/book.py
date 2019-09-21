# A function tightly coupled to an object
class Book:
    def __init__(self, title, subtitle, author):  # <1>
        self.title = title
        self.subtitle = subtitle
        self.author = author


def display_book_info(book):
    print(f'{book.title}: {book.subtitle} by {book.author}')  # <2>


# Coupling addressed by listening to the cohesion
class Book:
    def __init__(self, title, subtitle, author):
        self.title = title
        self.subtitle = subtitle
        self.author = author

    def display_info(self):  # <1>
        print(f'{self.title}: {self.subtitle} by {self.author}')  # <2>
