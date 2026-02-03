# Day 21: Simple Patient Management System
# ----------------------------------------
# ----plan --------------------
# 1- add patient in txt (name|age|their diagnosis)
# 2- read informatiom from txt and show it 
# 3- delete patient's information

# -----------------------------------------------------
# 1- add patient in txt (name|age|their diagnosis)
def add_patient():
  '''add patient's information'''
  print("~"*40)
  name=input("patient's name : ").strip().capitalize()
  while len(name)<1:
    name=input("please enter patient's name : ").strip().capitalize()
  while True:
    try:
      age =int(input("patient's age :"))
      if age<1:
        print("invalide age")
        continue
      break
    except ValueError:
      print("only numbers are aloweded")
  diagnosis=input("patient's diagnosis : ").strip()
  while not diagnosis:
    diagnosis=input("patient's diagnosis : ").strip()
  with open("patients.txt","a",encoding="utf-8")as file:
    file.write(f"{name}|{age}|{diagnosis}\n")
  with open("patients.txt","r",encoding="utf-8")as file:
    sort_list=file.readlines()
    sort_list.sort()
  with open("patients.txt","w",encoding="utf-8")as file:
    file.writelines(sort_list)
  print("information have been added")
# -----------------------------------------------
# 2- read informatiom from txt and show it 
def show_patients():
  try:
    with open("patients.txt","r",encoding="utf-8")as file:
      lines=file.readlines()
      if not lines :
        print("no data")
        return
      print("~"*40)
      for index,line in enumerate(lines,start=1):
        name,age,diagnosis=line.strip().split("|")
        print(f"{index} - name : {name} | age : {age} | diagnosis : {diagnosis}")
  except FileNotFoundError:
    print("no file data found")
# ---------------------------------
# 3- delete patient's information
def delete_patient():
  show_patients()
  with open("patients.txt","r",encoding="utf-8")as file:
    patient_list=file.readlines()
    
  while True:
    if len(patient_list)==0:
      break
    print('~'*40)
    delete_number=input("enter patient's number to delete or enter 'cancel' to back : ").strip()
    if delete_number == "cancel" :
      print("thank u")
      return
    
    if not delete_number.isdigit():
      print("invalid number choice")
      continue
    delete_number=int(delete_number)
    if delete_number > len(patient_list) or delete_number<1 :
      print(f"please try again enter from 1 to {len(patient_list)}")
      continue
    patient_list.pop(delete_number-1)
    with open ("patients.txt","w",encoding="utf-8") as file:
      file.writelines(patient_list)
    print("patients' information have been deleted")
    break
# --------------------
while True:
  print("~"*40)
  print("enter 0 to break")
  print("enter 1 to add patient")
  print("enter 2 to show patients")
  print("enter 3 to delete patient")
  choose=input("what is your choice ? ")
  while choose not in ("0","1","2","3"):
    choose=input("uncorect choice what is your choice ? ")
    
  if choose =="0":
    print('thank u . bye')
    break
  elif choose =="1":
    add_patient()
  elif choose =="2":
    show_patients()
  elif choose == "3":
    delete_patient()