class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Book "{book}" added!')

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'Book "{book}" removed!')
        else:
            print("Book not found!")

    def list_books(self):
        print("Available books:")
        for book in self.books:
            print(f'- {book}')

library = Library()
library.add_book("Python Basics")
library.add_book("Data Structures")
library.list_books()
library.remove_book("Python Basics")
library.list_books()
