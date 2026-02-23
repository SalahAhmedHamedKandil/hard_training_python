# library system
# ============================================
import json
FILE_NAME=r"D:\elzero_python\json_practice\library\library.json"
def load_data():
    try:
        with open (FILE_NAME,"r",encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("file not found")
        return{}
# =================================
def save_data(data):
    with open(FILE_NAME,"w",encoding="utf-8")as file:
        json.dump(data,file,indent=4)
# ===================================
def add_book():
    data=load_data()
    while True:
        print("enter 'exit' to exit")
        book_name=input("enter book's name : ").strip().lower()
        if not book_name:
            print("please enter book's name or 'exit' to exit. ")
            print("~"*30)
            continue
        if book_name =="exit":
            print("bye")
            print("~"*30)
            return
        if book_name in data:
            print("the book aleardy exists. ")
            print("~"*30)
            return
        break
    while True:
        print("enter 'exit' to exit")
        total=input("enter book's number : ").strip().lower()
        if not total:
            print("please enter book's number or 'exit' to exit ")
            print("~"*30)
            continue
        if total =="exit":
            print("bye")
            print("~"*30)
            return
        if not total.isdigit():
            print("invalid number try again")
            continue
        total=int(total)
        print("~"*30)
        break
    available=total
    borrowed=total-available
    data[book_name]={
        "total":total,
        "available":available,
        "borrowed":borrowed
                     }
    save_data(data)
    print("book added successfully")
        
# ========================================
def show_books():
    data=load_data()
    if not data:
        print("library is empty")
        return
    for index,(name,name_info) in enumerate(data.items(),start=1):
        print(
            f"{index}- "
            f"name: {name} | "
            f"total: {name_info['total']} | "
            f"available: {name_info['available']} | "
            f"borrowed: {name_info['borrowed']}"
        )
# ==========================================================
def borrow_book():
    data = load_data()
    show_books()
    if not data:
        print("we don't have books to borrow")
        print("~"*30)
        return
    while True:
        print("enter 'exit' to exit")
        name_book=input("enter book's name to borrow or 'exit' : ").lower().strip()
        if name_book=="exit":
            print ("bye")
            print("~"*30)
            return
        if name_book not in data:
            print("we didn't have this book ")
            print("~"*30)
            continue
        book_data=data[name_book]
        if book_data["available"]==0:
            print("all book's copies have been borrowed",
                  "choose another one please")
            print("~"*30)
            continue
        break
    while True:
        borrowed_number=input("how many books u want? or exit to exit : ").strip()
        if borrowed_number=="exit":
            print("bye")
            print("~"*30)
            return
        if not borrowed_number.isdigit():
            print("invalid number",
                  "just numbers")
            print("~"*30)
            continue
        borrowed_number=int(borrowed_number)
        if borrowed_number <= 0:
            print("number must be greater than zero")
            print("~"*30)
            continue
        if book_data["available"]<borrowed_number:
            print(f"we jjust have {book_data['available']}",
                  "try again ")
            print("~"*30)
            continue
        break
    book_data["available"] -= borrowed_number
    book_data["borrowed"] += borrowed_number

    save_data(data)
    print("books borrowed successfully")
# ===================================================
def return_book():
    data = load_data()
    show_books()
    if not data:
        print("we don't have books to borrow")
        print("~"*30)
        return
    while True:
        print("enter 'exit' to exit")
        name_book=input("enter book's name to return or 'exit' : ").lower().strip()
        if name_book=="exit":
            print ("bye")
            print("~"*30)
            return
        if name_book not in data:
            print("we didn't have this book,enter correct name ")
            print("~"*30)
            continue
        book_data=data[name_book]
        if book_data["borrowed"]==0:
            print("all book's copies are aleady here",
                  "choose another one please")
            print("~"*30)
            continue
        break
    while True:
        return_number=input("how many books u will return ? or exit to exit : ").strip()
        if return_number=="exit":
            print("bye")
            print("~"*30)
            return
        if not return_number.isdigit():
            print("invalid number",
                  "just numbers")
            print("~"*30)
            continue
        return_number=int(return_number)
        if return_number <= 0:
            print("number must be greater than zero")
            print("~"*30)
            continue
        if book_data["borrowed"]<return_number:
            print(f"we just have borrowed {book_data['borrowed']}",
                  "try again ")
            print("~"*30)
            continue
        break
    book_data["available"] += return_number
    book_data["borrowed"] -= return_number
    save_data(data)
# ===============================================
def delete_books():
    show_books()
    data=load_data()
    if not data:
        print("library is empty")
        print("~"*30)
        return
    while True:
        delete_book=input("enter book name to delete it or exit to exit : ")
        if delete_book=="exit":
            print("bye")
        if delete_book not in data:
            print("we didn't have this book"
                  "try again")
            continue
        break
    del data[delete_book]
    save_data(data)
    print("the book have been deleted")
        


            
# ==================================================
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
        elif choice =="4":
            return_book()
        elif choice=="5":
            delete_books()
        elif choice == "6": 
            print("thank u")
            break
main()
    
