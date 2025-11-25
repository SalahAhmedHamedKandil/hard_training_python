# we are goin to read information from "read.txt"

# open read.txt
import os

with open ("read.txt","r") as file:
  all_info=file.read()
  print(all_info) # print all file as one tring 
  print("-_"*9)
  #  the result
  # 1 = one 
  # 2 = two
  # 3 = three
  # 4 = four
  # 5 = five
  # 6 = six

# ---------------------------------

with open ("read.txt","r") as file:
  for line in file :
    print(f"line {line.strip()}")
  print("-_"*9)

#  the result
# line 2 = two
# line 3 = three
# line 4 = four
# line 5 = five
# line 6 = six
# ---------------------------------
with open ("read.txt","r") as file:
   for lines in file.readlines():
     print(lines)
   print("-_"*9)

#  the result
# 1 = one

# 2 = two

# 3 = three

# 4 = four

# 5 = five

# 6 = six
#----------------------------------

with open ("read.txt","r") as file:
 for line in file :
  # line = line.strip()
  if "=" in line:
    key,value=line.strip().split("=",1)
    print(f"{key} = {value}")
#  the result
    # 1  =  one
    # 2  =  two
    # 3  =  three
    # 4  =  four
    # 5  =  five
    # 6  =  six

   
def load_menu():
  menu={}
  if os.path.exists("read.txt"):
    with open("read.txt","r") as file:
      lines=file.readlines()
      for line in lines:
        if "=" in line:
          key,value = line.strip().split("=")
          menu[key]=int(value)
  return menu
qq=load_menu()
print(f"sss{qq}") # output sss{'one ': 1, 'two ': 2}


