# iterable vs iterator
# -----------------
# iterable 
# 1-object contains data that can be iterated upon
# 2-example (string,list,tuble,dict,set)
# ----------------------------------------
# iterator
# 1-object used to iterate over iterable using next() method return 1 element a time
# 2-u can generate iterator from iterabe wehen usin iter() method
# 3-for loop already calls iter() nethod on the iterable behind the scene
# 4-gives "stopiteration" if there is no next element
# ---------------------------------------------
mystring="salah" # iterable cause we can loop in salah
for numb, letter in enumerate(mystring,start=1):
  print(f"{numb}-{letter}")
#output
# 1-s
# 2-a
# 3-l
# 4-a
# 5-h  
for numb, letter in enumerate(mystring,start=1):  
  print(f"{numb}-{letter}",end=" ")
# output 
# 1-s 2-a 3-l 4-a 5-h
# -------------------------
myNumber=11 # it is iterator
# for n in myNumber:
#   print(myNumber)
#   # output => TypeError: 'int' object is not iterable
print("\n")
print("/"*30)
# print(next(mystring)) # => TypeError: 'str' object is not an iterator

myiterator=iter(mystring)
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))



