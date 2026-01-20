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

  with open("patients.txt","a",encoding="utf-8")as file:
    file.write(f"{name}|{age}|{diagnosis}\n")
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
      for line in lines:
        name,age,diagnosis=line.strip().split("|")
        print(f"name:{name},age:{age},diagnosis:{diagnosis}")
  except ValueError:
    print("no file data found")





# --------------------
add_patient()
show_patients()