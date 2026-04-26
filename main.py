from book import Book
from member import Member
from library import Library

# Kreiramo biblioteku
library = Library("City Library")

# Dodajemo knjige
book1 = Book("1984", "George Orwell", "ISBN001")
book2 = Book("Brave New World", "Aldous Huxley", "ISBN002")
library.add_book(book1)
library.add_book(book2)

# Dodajemo člana
member1 = Member("Nenad Miljkovic", "M001")
library.add_member(member1)

# Član pozajmljuje knjigu
member1.borrow_book(book1)

# Ispis stanja
print("Books in library:")
print(library.list_books())

print("\nMembers:")
print(library.list_members())

# Član vraća knjigu
member1.return_book(book1)
print("\nBooks after return:")
print(library.list_books())
