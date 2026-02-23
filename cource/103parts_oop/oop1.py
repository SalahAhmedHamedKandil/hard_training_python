# oop =object oriented programing
# --------------------------------
class Book:
    title=""        #attributes
    author=""       #attributes
    pages=0         #attributes
    
    pass
my_book=Book() #object
my_book.title="origin"
my_book.author="Dan brown"
my_book.pages=100
print(my_book.title,
      my_book.author,
      my_book.pages,
      sep="\n")
# ===========================
secon_book=Book() #object
secon_book.title="how"
secon_book.author="Salah"
secon_book.pages=111
print(secon_book.title,
      secon_book.author,
      secon_book.pages,
      sep="\n")