# add expences (discription,cost) 
# show expences 



# --------------------------------
# add expences
import os
from datetime import datetime
def add_expences():
  while True:
    try:
      cost=float(input("enter expencs amount : ").strip())
      break
    except ValueError:
      print("invalid number.try again.")
  discription=input("enter the discription : ").strip()
  now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  with open("expences.txt","a")as file:
    file.write(f"{cost},{discription},{now}\n")
    print("item is add")
    
add_expences()
# ------------------------------
def show_expences():
  with open ("expences.txt","r")as file:
    for line in file:  
      cost,information,date=line.strip().split(",")
      print(f"{information} => {cost} => {date}")
show_expences()