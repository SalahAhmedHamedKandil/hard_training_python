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
            continue
        if book_name =="exit":
            print("bye")
            return
        if book_name in data:
            print("the book aleardy exists. ")
            return
        break
    while True:
        print("enter 'exit' to exit")
        total=input("enter book's number : ").strip().lower()
        if not total:
            print("please enter book's number or 'exit' to exit ")
            continue
        if total =="exit":
            print("bye")
            return
        if not total.isdigit():
            print("invalid number try again")
            continue
        total=int(total)
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

show_books()
