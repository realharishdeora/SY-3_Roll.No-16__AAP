class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f"Book '{title}' added.")

    def register_patron(self, name):
        self.patrons.append(Patron(name))
        print(f"Patron '{name}' registered.")

    def borrow_book(self, patron_name, book_title):
        for patron in self.patrons:
            if patron.name == patron_name:
                for book in self.books:
                    if book.title == book_title and book.available:
                        book.available = False
                        patron.borrowed_books.append(book)
                        print(f"{patron_name} borrowed '{book_title}'.")
                        return
                print("Book not available.")
                return
        print("Patron not found.")

    def return_book(self, patron_name, book_title):
        for patron in self.patrons:
            if patron.name == patron_name:
                for book in patron.borrowed_books:
                    if book.title == book_title:
                        book.available = True
                        patron.borrowed_books.remove(book)
                        print(f"{patron_name} returned '{book_title}'.")
                        return
                print("Book not borrowed by patron.")
                return
        print("Patron not found.")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"{book.title} by {book.author} - {status}")


# Driver Code
library = Library()

library.add_book("Onepiece", "Echiro Oda")
library.add_book("Data Structures", "Mark")

library.register_patron("Harish")

library.borrow_book("Harish", "Onepiece")
library.display_books()

library.return_book("Harish", "Onepiece")
library.display_books()


'''Output
Book 'Data Structures' added.
Patron 'Harish' registered.
Harish borrowed 'Onepiece'.

Library Books:
Onepiece by Echiro Oda - Borrowed
Data Structures by Mark - Available
Harish returned 'Onepiece'.

Library Books:
Onepiece by Echiro Oda - Available
Data Structures by Mark - Available'''