# add expenses (discription,cost) 
# show expenses 



# --------------------------------
# add expenses
import os
from datetime import datetime
def add_expenses():
  while True:
    try:
      cost=float(input("enter expencs amount : ").strip())
      break
    except ValueError:
      print("invalid number.try again.")
  discription=input("enter the discription : ").strip()
  now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  with open("expenses.txt","a")as file:
    file.write(f"{cost},{discription},{now}\n")
    print("item is add")
    
# add_expenses()
# ------------------------------
def show_expenses():
  with open ("expenses.txt","r")as file:
    total_cost=0
    for number,line in enumerate(file,start=1):  
      cost,information,date=line.strip().split(",")
      total_cost +=float(cost)
      print(f"{number}-{information} => cost:{cost} =>date:{date}")
    print(f"total cost {total_cost}")
# show_expenses()
# ----------------------------
def delete_item():
  if not os.path.exists("expenses.txt")or os.path.getsize("expenses.txt")==0:
    print ("no items to delete")
    return
  show_expenses()
  with open("expenses.txt","r")as file:
    data=file.readlines()
    while True:
      try:
        delete=int(input("enter item number to delete : ").strip())
        if delete>len(data) or  delete<1:
          print("out of the range") 
        else:
          break
      except ValueError:
        print("invalid number,try again.")
    deleted=data.pop(delete-1)
    print("we deleted it")
  with open("expenses.txt","w")as file:
    file.writelines(data)
# ------------------------------------------
while True:
  print("`"*40)
  choose = input("enter 1 to add expenses\nenter 2 to show expenses\nenter 3 to delete expenses \nenter 0 to close\nenter your choice : ")
  while choose not in ("1","2","3","0"):
    print("`"*40)
    choose = input("please choose from this choice\nenter 1 to add expenses\nenter 2 to show expenses\nenter 3 to delete expenses \nenter 0 to close\nenter your choice : ")

  print("`"*40)
  if choose =="1":
    add_expenses()
  elif choose == "2":
    show_expenses()
  elif choose =="3":
    delete_item()
  elif choose =="0":
    print("bye")
    break