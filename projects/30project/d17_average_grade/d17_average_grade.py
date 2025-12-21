# average grade calcukator
# ----------------------------
# 1 - enter all information 
# 2 - calculate 
# ---------------------------------
import os
print ("welcome")
def add_information ():
  print("~"*40)

  name=input("enter student's name :")
  while True:
    try:
      english=float(input("what are the grades in english : ").strip())
      break
    except ValueError:
      print("invalid number ,try again")
  while True:
    try:
      Arabic=float(input("what are the grades in Arabic : ").strip())
      break
    except ValueError:
      print("invalid number ,try again")
  while True:
    try:
      history=float(input("what are the grades in history : ").strip())
      break
    except ValueError:
      print("invalid number ,try again")
  while True:
    try:
      science=float(input("what are the grades in science : ").strip())
      break
    except ValueError:
      print("invalid number ,try again")
  with open("d17_average_grade.txt","a") as file:
    file.write(f"{name}|{english}|{Arabic}|{history}|{science}\n")
    print("information have been added")
# -------------------------------------------
def average_calculator():
  print("~"*40)
  if not os.path.exists("d17_average_grade.txt"):
    print("print file not exists")
  elif os.path.getsize("d17_average_grade.txt")==0:
    print("file is empty")
  else:
    try:
      with open("d17_average_grade.txt","r")as file:
        for line in file :
          line=line.strip()
          if not line or "|" not in line:
            continue
          s1,s2,s3,s4,s5=line.split("|")
          average=((float(s5)+float(s2)+float(s3)+float(s4))/400)
          print(f"{s1} average = {average}")
    except:
      print("error")


while True:
  print("~"*40)
  print("enter 0 to close")
  print("enter 1 to add studet ")
  print("enter 2 see average all student")
  # print("enter ")
  choose =input("enter your choice : ").strip()
  if choose =="0":
    print('bye')
    break
  elif choose =="1":
    add_information()
  elif choose =="2":
    average_calculator()
