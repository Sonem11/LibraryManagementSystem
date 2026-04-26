from book import Book
from member import Member

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def list_books(self):
        return [f"{b.title} by {b.author} - {'Borrowed' if b.is_borrowed else 'Available'}" for b in self.books]

    def list_members(self):
        return [f"{m.name} (ID: {m.member_id})" for m in self.members]
