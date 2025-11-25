# main menu
# Menue = Menu
# menue_r = show_menu
#  menue = menu1



# ---------------------------------------
import os
# 1 load menu
def load_menu():
  menu={}
  
  #لو الملف موجود هنفتحة
  if os.path.exists("new_menu1.txt"):
    with open("new_menu1.txt","r") as file:
      lines = file.readlines() 
      if len(lines) ==0:
          menu={"tea":10,
          "coffee":25
          }
          save_menu(menu)
          return menu    
    for line in lines:
        if "=" in line:
          item, price = line.strip().split("=")
          menu[item]=int(price)
          # print(menu)
  else:
    #لو الملف مش موجود
    menu={"tea":10,
          "coffee":25
          }
    
    save_menu(menu)
  return menu

#  save menu into txt 
def save_menu(menu):
  with open("new_menu1.txt","w") as file:
    for item , price in menu.items():
      file.write(f"{item}={price}\n")
      

Menu=load_menu()
ur_name=input("what is ur name ? ").strip().capitalize()

def show_menu(welcome,**menu1):
  print("*"*20)
  print(f"hello {welcome} \nchoose from our items .")
  for item , price in menu1.items():
    print(f"{item} => {price} pounds")
  print("*"*20)
    
def edit_menu():
  global Menu
  while True:
    print("\n --edit menu mode --")
    print("1 - add item")
    print("2 - edit item price")
    print("3 - delet item")
    print("4 - show menu")
    print("5 - exit edit mode")
    choice=input("what is choice number ?").strip()
    if choice =="1":
      item=input("enter new item name : ").strip().lower()
      price=int(input("enter new item price : "))
      Menu[item]=price
      save_menu(Menu)
      print(f"{item} is add")
    elif choice == "2":
      item=input("item name to edit : ")
      if item in Menu:
        new_price=int(input("enter new price : "))
        Menu[item]=new_price
        save_menu(Menu)
        print("new price is saved")
      else:
        print(f"{item} is not in menu")
    elif choice == "3" :
      item=input("item name to delete : ").strip()
      if item in Menu:
        del Menu[item]
        save_menu(Menu)
        print(f"{item} is deleted")
      else:
        print(f"{item} is not in menu")
    elif choice == "4":
      show_menu("salah",**Menu)
    elif choice == "5":
      break
    else:
      print("invalid option")

#-----  order menu -----
def choose_order():
  show_menu(ur_name,**Menu)
  orders=[]
  total=0
  while True:
    order=input("enter ur choice from menu or done to finsg : ")
    if order == "done":
      print("thank u for ur visi")
      break
    if order in Menu :
      orders.append(order)
      total +=Menu[order]
      print(f"{order} added & total cost {total}")
    else:
      print("invalid order")
      show_menu(ur_name,**Menu)
  print("\nur order is:")
  for o in orders:
    print (f"{o} => {Menu[o]} pounds")
  print("-_"*20)
  print(f"total cost = {total}")
  print("-_"*20)


# -----------------------------------
admins=["admin"]
password="admin"
if ur_name.lower() in admins :
  password_menu=input(f"enter the password : ")
  if password == password_menu:
    edit_menu()
  else:
    print ("rong password")

else:
  choose_order()