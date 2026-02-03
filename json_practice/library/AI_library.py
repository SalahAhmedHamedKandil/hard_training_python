import json

FILE_NAME = r"D:\elzero_python\json_practice\library\AI_library.json"


# =============================
# Load data from json file
# =============================
def load_data():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


# =============================
# Save data to json file
# =============================
def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


# =============================
# Add new book
# =============================
def add_book():
    data = load_data()

    name = input("Enter book name: ").strip().lower()
    if name in data:
        print("Book already exists ❌")
        return

    total = int(input("Enter total copies: "))

    data[name] = {
        "total": total,
        "available": total
    }

    save_data(data)
    print("Book added successfully ✅")


# =============================
# Show all books
# =============================
def show_books():
    data = load_data()

    if not data:
        print("Library is empty 📭")
        return

    for book, info in data.items():
        print(f"{book} → Total: {info['total']} | Available: {info['available']}")


# =============================
# Borrow book
# =============================
def borrow_book():
    show_books()
    data = load_data()
    name = input("Enter book name: ").strip().lower()

    if name not in data:
        print("Book not found ❌")
        return

    if data[name]["available"] > 0:
        data[name]["available"] -= 1
        save_data(data)
        print("Book borrowed successfully 📘")
    else:
        print("No available copies ❌")


# =============================
# Return book
# =============================
def return_book():
    data = load_data()
    name = input("Enter book name: ").strip().lower()

    if name not in data:
        print("Book not found ❌")
        return

    if data[name]["available"] < data[name]["total"]:
        data[name]["available"] += 1
        save_data(data)
        print("Book returned successfully 🔁")
    else:
        print("All copies are already in library ❌")


# =============================
# Delete book
# =============================
def delete_book():
    data = load_data()
    name = input("Enter book name: ").strip().lower()

    if name in data:
        del data[name]
        save_data(data)
        print("Book deleted successfully 🗑️")
    else:
        print("Book not found ❌")


# =============================
# Main menu
# =============================
def main():
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
            add_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice ❌")


main()
