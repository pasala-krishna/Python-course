class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. Title: {book.title}, Author: {book.author}")

# Example usage:
library = Library()

library.add_book("Book 1", "Author 1")
library.add_book("Book 2", "Author 2")
library.add_book("Book 3", "Author 3")

library.display_books()
