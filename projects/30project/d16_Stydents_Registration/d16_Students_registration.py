# student registration system
# ---------------------------------
# 1- add students in txt file (age,grade)
# 2- read information from txt file 
# 3- edite information (delete or edite)
# ----------------------------------------
import os
# add student
def add_student():
  name=input("student's name ? ").capitalize().strip()
  while len(name)==0:
    print ("u didn't enter name")
    name=input("student's name ? ").capitalize().strip()
  while True:
    try:
      age=int(input("student's age ?"))
      break
    except ValueError:
      print("try again invalid age number")
  with open("student_info.txt","a") as file:
    file.write(f"{name}|{age}\n")
# -----------------------------------
# read information
def read_information():
    if not os.path.exists("student_info.txt")or os.path.getsize("student_info.txt")==0:
       print("the file is empy or not exists")
    else:
      try:
          with open("student_info.txt","r") as file:
              for index, line in enumerate(file, start=1):
                  line = line.strip()
                  if not line or "|" not in line:
                      continue
                  name, age = line.split("|")
                  print(f"{index}- student's name : {name} , his age : {age}")
      except FileNotFoundError:
          print("no students found")

# ------------------------------------
# save
def save(students):
  with open("student_info.txt","w") as file:
    for student in students:
        file.write(student)
# -------------------------------------
# delete 
def delete_student():
  if not os.path.exists("student_info.txt")or os.path.getsize("student_info.txt")==0:
       print("the file is empy or not exists")
  else:
    read_information()
    while True:
      try:
        student_number=int(input("enter student's number to delete : "))
        break
      except ValueError:
        print("please try again invalid student number number ")
    with open("student_info.txt","r") as file:
      info=file.readlines()
      info.pop(student_number-1)
    save(info)
# --------------------------------------------
while True:
  print("~"*40)
  print("enter 0 to close")
  print("enter 1 to add student")
  print("enter 2 to show students")
  print("enter 3 to delete student")
  choose=input("enter your choice : ")
  while choose not in ("0","1","2","3"):
    choose=input("enter your choice : ")
  if choose =="0":
    print("bye")
    break
  elif choose =="1":
    add_student()
  elif choose =="2":  
    read_information()
  elif choose =="3":
    delete_student()