class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.is_borrowed=False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed=True
            return True
        return False
    
    def return_book(self):
        self.is_borrowed=False

class Patron:
    def __init__ (self, name, patron_id):
        self.name=name
        self.patron_id=patron_id
        self.borrowed_books=[]

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def register_patron(self, patron):
        self.patrons.append(patron)

    def borrow_book(self, patron_id, isbn):
        patron = next((p for p in self.patrons if p.patron_id == patron_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)
        if patron and book:
            patron.borrow_book(book)
        else:
            print("Patron or Book not found.")

    def return_book(self, patron_id, isbn):
        patron = next((p for p in self.patrons if p.patron_id == patron_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)

        if patron and book:
            patron.return_book(book)
        else:
            print("Patron or Book not found.")

library=Library()

b1=Book("HarryPotter","JK Rowling",101)
b2=Book("500Days of Summer","idk",102)

library.add_book(b1)
library.add_book(b2)

p1=Patron("Harish","P001")
p2=Patron("Avinash","P002")

library.register_patron(p1)
library.register_patron(p2)

library.borrow_book("P001", 101)
library.borrow_book("P002", 101)

library.return_book("P001", 101)

print("\nLibrary Books:")
for book in library.books:
    status = "Borrowed" if book.is_borrowed else "Available"
    print(f"{book.title} - {status}")

print("\nPatron Details:")
for patron in library.patrons:
    print(f"{patron.name}: {[book.title for book in patron.borrowed_books]}")