import warnings


# Initial version
class Book:
    def __init__(self, data):
        self.title = data['title']  # <1>
        self.subtitle = data['subtitle']

        if self.title and self.subtitle:  # <2>
            self.display_title = f'{self.title}: {self.subtitle}'
        elif self.title:
            self.display_title = self.title
        else:
            self.display_title = 'Untitled'


# Setter version
class Book:
    def __init__(self, data):
        self.title = data['title']
        self.subtitle = data['subtitle']
        self.set_display_title()  # <1>

    def set_display_title(self):  # <2>
        if self.title and self.subtitle:
            self.display_title = f'{self.title}: {self.subtitle}'
        elif self.title:
            self.display_title = self.title
        else:
            self.display_title = 'Untitled'


# @property version
class Book:
    def __init__(self, data):
        self.title = data['title']
        self.subtitle = data['subtitle']

    @property
    def display_title(self):  # <1>
        if self.title and self.subtitle:
            return f'{self.title}: {self.subtitle}'
        elif self.title:
            return self.title
        else:
            return 'Untitled'


# With embedded author data
class Book:
    def __init__(self, data):
        # ...

        self.author_data = data['author']  # <1>

    @property
    def author_for_display(self):  # <2>
        return f'{self.author_data["first_name"]} {self.author_data["last_name"]}'

    @property
    def author_for_citation(self):  # <3>
        return f'{self.author_data["last_name"]}, {self.author_data["first_name"][0]}.'


# With extracted author class
class Author:
    def __init__(self, author_data):  # <1>
        self.first_name = author_data['first_name']
        self.last_name = author_data['last_name']

    @property
    def for_display(self):  # <2>
        return f'{self.first_name} {self.last_name}'

    @property
    def for_citation(self):
        return f'{self.last_name}, {self.first_name[0]}.'


class Book:
    def __init__(self, data):
        # ...

        self.author_data = data['author']  # <3>
        self.author = Author(self.author_data)  # <4>

    @property
    def author_for_display(self):  # <5>
        warnings.warn('Use book.author.for_display instead', DeprecationWarning)
        return self.author.for_display

    @property
    def author_for_citation(self):
        warnings.warn('Use book.author.for_citation instead', DeprecationWarning)
        return self.author.for_citation
