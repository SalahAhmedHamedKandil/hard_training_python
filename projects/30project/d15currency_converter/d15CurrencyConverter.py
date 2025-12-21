# Currency Converter
# ------------------------------
# plan
# 1 function choose the currency
# 2 function to add your amount of your currency
# -------------------------------------------- 
# all currencies based on USD
# ---------------------------------------
# ADD CURRNCY TO TXT
import os
def add_currencies():
  name_currency=input("enter name currncy : ").strip().upper()
  while name_currency=="":
    print("please enter the name of currncy .")
    name_currency=input("enter name currncy : ").strip().upper()
  while True:
    try:
      value_currency=float(input("enter value of currncy based od USD : ").strip())
      break
    except ValueError:
      print("\ninvalid number try again\n")
  with open ("currency_conveter.txt","a") as file:
    file.write(f"{name_currency}|{value_currency}\n")
# --------------------------------------------------------
# make a dict contain currencies
currencies={}
def dict_currency():
  global currencies
  currencies={}
  with open ("currency_conveter.txt","r") as file:
    for line in file:
      currency,value=line.strip().split("|")
      
      currencies[currency]=float(value)
# currencies=dict_currency()
#----------------------------------------------------------------
def showw_currencyies(): 
  with open ("currency_conveter.txt","r") as file:
    for line in file:
      currency,value=line.strip().split("|")
      print(f"{currency} => {value}")
# -----------------------------
def currency_converter():
  dict_currency()  
  showw_currencyies()
  source_currency=input("what currency do u have ?").upper()
  while True :
    try:
      amount=float(input("what currency amount do u have ?").strip())
      break
    except ValueError:
      print("invalid number try agai")
  taget_currency=input("what currncy do u want ?").upper()
  result=(float(amount)/float(currencies[source_currency])*float(currencies[taget_currency]))
  print(f"{result:.2f}")
# --------------------------    
while True:
  print('~'*40)
  print("enter 0 to close")  
  print("enter 1 to add currency")  
  print("enter 2 to show currency price")  
  print("enter 3 to currency_converter")  
  choose=input("enter youyur choice : ").lower().strip()
  while choose not in ("0","1","2","3"):
    choose=input("enter youyur choice again please : ").lower().strip()
  if choose == "0":
    print("bye")
    break
  elif choose =="1":
    add_currencies()
  elif choose == "2":
    showw_currencyies()
  elif choose == "3":
    currency_converter()
