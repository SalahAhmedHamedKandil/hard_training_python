# add new book (name | how many books? | number of book available)
# show all books
# search book
# borrow book
# return book
# delete book
# =======================================
library=r"D:\elzero_python\projects\30project\d22mini_liprary_management_system\library_system.txt"
def add_book():
    while True:
        print("enter cancel to close operation")
        book_name=input("enter new book name : ").strip().lower()
        if len (book_name) >1 and book_name!= "cancel":
            Book_name=book_name
            break
        if len(book_name)<1:
            print("please enter the name of the book or enter 'cancel' to close")
        if book_name=="cancel":
            print("bye")
            return
    while True:
        books_number=input("how many books ?")
        if books_number =="cancel":
            print("bye")
            return
        if not books_number.isdigit() :
             print("invalid number")
             continue
        books_number=int(books_number)
        if books_number<1 :
             print("please enter  number equal or more than 1")
             continue
        break
    available_books=books_number
    borrow_books=books_number-available_books
   
    with open(library,"a",encoding="utf-8") as  file:
        file.write(f"{Book_name}|{books_number}|{available_books}|{borrow_books}\n")
    with open(library,"r",encoding="utf-8") as  file:
        books_list=file.readlines()
        books_list.sort()
    with open(library,"w",encoding="utf-8") as file:
        file.writelines(books_list)
        print("books has been added")

# add_book()
# =========================================
# show books
def show_books():
    print("~"*40)
    try:
        with open (library,"r",encoding="utf-8") as file:
            books_list=file.readlines()
            if not books_list:
                print("no data")
                return
            for index,books in enumerate(books_list,start=1):
                name,o_number,a_number,b_number=books.strip().split("|")
                print(f"({index}) book's name : {name} ")
                print(f"number of books : {o_number} ")
                print(f"available books : {a_number} ")
                print(f"borrow books : {b_number} ")
                print("~"*40)
    except FileNotFoundError:
        print("we didn't find data file")

# ==============================================
def borrow_books():
    show_books()
    with open (library,"r",encoding="utf-8") as file:
        books_list=file.readlines()
        if not books_list:
            print("we don't have book to borrow")
            return
    while True:
        print("enter 'cancel' to exit ")
        book_=input("what is the book number ? ").strip()
        if book_ =="cancel":
            print ("bye")
            return
        if not book_.isdigit():
            print("unvalid number")
            continue
        book_=int(book_)

        if 1>book_ or book_>len(books_list):
            print("we do have book whith this number , try again")
            continue
        the_book=books_list[book_-1]
        name,o_number,a_number,b_number=the_book.strip().split("|")
        o_number = int(o_number)
        a_number = int(a_number)
        b_number = int(b_number)        
        if a_number==0:
            print(f"this book ({name}) is unavailable now.choose another one please")
            continue
        break
    while True:
        print("enter 'cancel' to exit ")
        copies=input("how many copies ? ").strip()
        if copies =="cancel":
            print ("bye")
            return
        if not copies.isdigit():
            print("unvalid number")
            continue
        copies=int(copies)
        if 1>copies :
            print("enter positive number")
            continue
        if copies>a_number:
            print(f"this amount {copies} un available")
            print(f"we just have {a_number}")
            continue
        break
    a_number = a_number - copies
    b_number = b_number + copies
    books_list[book_-1] = f"{name}|{o_number}|{a_number}|{b_number}\n"
    with open(library, "w", encoding="utf-8") as file:
        file.writelines(books_list)

    print("book borrowed successfully ✅")
#=======================================
def return_book():
    print("enter 'cancel'to exit")
    show_books()
    with open(library,"r",encoding="utf-8")as file:
        list_book=file.readlines()
        if not list_book:
            print("we don't have book to borrow")
            return
    while True:
        book_number=input("enter book's number to return it :").strip()
        if book_number =="cancele":
            print("bye")
            return
        if not book_number.isdigit():
            print("unvalid umber")
            continue
        book_number=int(book_number)
        if book_number>len(list_book)or book_number<1:
            print(f"our books start from 1 to {len(list_book)} try again ")
            return
        the_book=list_book[book_number-1]
        name,o_number,a_number,b_number=the_book.strip().split("|")
        o_number = int(o_number)
        a_number = int(a_number)
        b_number = int(b_number)
        if the_book==o_number:
            print(f"({book_number})-{name} we have all copies,there a proplem")
            continue
        break
    while True:
        copies=input("how many copies to return? ").strip()
        if copies =="cancel":
            print ("bye")
            return
        if not copies.isdigit():
            print("unvalid number")
            continue
        copies=int(copies)
        if 1>copies :
            print("enter positive number")
            continue
        if copies>b_number:
            print(f"this amount  is more than borrowed copies")
            print(f"we just borrowed {b_number}")
            continue
        break
    a_number=a_number+copies
    b_number=b_number-copies
    list_book[book_number-1]=f"{name}|{o_number}|{a_number}|{b_number}\n"
    with open(library,"w",encoding="utf-8")as file:
        file.writelines(list_book)






# =======================================
while True:
    print("~"*40)
    print("enter 0 to break")
    print("enter 1 to add book")
    print("enter 2 to show book")
    print("enter 3 to borrow book")
    print("enter 4 to return book")
    choose=input("what is your choice ? ")
    while choose not in ("0","1","2","3","4"):
        choose=input("uncorect choice what is your choice ? ")
    
    if choose =="0":
        print('thank u . bye')
        break
    elif choose =="1":
        add_book()
    elif choose =="2":
        show_books()
    elif choose == "3":
        borrow_books()
    elif choose == "4":
        return_book()
    