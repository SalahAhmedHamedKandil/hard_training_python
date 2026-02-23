
# class Book:
#     def __init__(self,title,author,pages):
#         self.title=title
#         self.author=author
#         self.pages=pages
#         # pass

# def add_book():
#     title=input("book's title : ")
#     author=input("book's author :")
#     pages=input("book's pages : ")
#     return Book(title,author,pages)

# my_book=add_book()
# print( f"my book is {my_book.title} and the author {my_book.author} have {my_book.pages} pages" )


# =======================================================
import json


class Book:
    def __init__(self, name, total):
        self.name = name
        self.total = total
        self.available = total
        self.borrowed = 0

    def to_dict(self):
        return {
            "total": self.total,
            "available": self.available,
            "borrowed": self.borrowed
        }


class Library:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4)

    def add_book(self):
        name = input("Enter book name: ").strip().lower()

        if name in self.data:
            print("Book already exists.")
            return

        total = input("Enter total number of books: ")

        if not total.isdigit():
            print("Invalid number.")
            return

        total = int(total)

        book = Book(name, total)
        self.data[name] = book.to_dict()

        self.save_data()
        print("Book added successfully.")

    def show_books(self):
        if not self.data:
            print("Library is empty.")
            return

        for index, (name, info) in enumerate(self.data.items(), start=1):
            print(
                f"{index}- {name} | "
                f"Total: {info['total']} | "
                f"Available: {info['available']} | "
                f"Borrowed: {info['borrowed']}"
            )

    def borrow_book(self):
        name = input("Enter book name to borrow: ").strip().lower()

        if name not in self.data:
            print("Book not found.")
            return

        book = self.data[name]

        if book["available"] == 0:
            print("No copies available.")
            return

        amount = input("How many copies? ")

        if not amount.isdigit():
            print("Invalid number.")
            return

        amount = int(amount)

        if amount > book["available"]:
            print("Not enough copies.")
            return

        book["available"] -= amount
        book["borrowed"] += amount

        self.save_data()
        print("Borrow successful.")

    def return_book(self):
        name = input("Enter book name to return: ").strip().lower()

        if name not in self.data:
            print("Book not found.")
            return

        book = self.data[name]

        if book["borrowed"] == 0:
            print("No borrowed copies.")
            return

        amount = input("How many copies to return? ")

        if not amount.isdigit():
            print("Invalid number.")
            return

        amount = int(amount)

        if amount > book["borrowed"]:
            print("Return amount exceeds borrowed.")
            return

        book["available"] += amount
        book["borrowed"] -= amount

        self.save_data()
        print("Return successful.")

    def delete_book(self):
        name = input("Enter book name to delete: ").strip().lower()

        if name not in self.data:
            print("Book not found.")
            return

        del self.data[name]
        self.save_data()
        print("Book deleted.")

    def menu(self):
        while True:
            print("""
==============================
 Library Management System
==============================
1- Add book
2- Show all books
3- Borrow book
4- Return book
5- Delete book
6- Exit
""")

            choice = input("Choose option: ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.show_books()
            elif choice == "3":
                self.borrow_book()
            elif choice == "4":
                self.return_book()
            elif choice == "5":
                self.delete_book()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")


# ===== Run Program =====
library = Library("library.json")
library.menu()

