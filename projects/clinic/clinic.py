# patient mange

# --------------------------------------
# 1-we will define function to add patient
patients="patients.txt"
def add_patient():
  name=input("enter the name : ")
  age =input("enter the age : ")
  diagnosis =input("enter the diagnosis : ")
  medicine =input("enter medicin : ")
  with open (patients,"a",encoding="utf-8") as file:
    file.write(name + "," + age + "," + diagnosis + "," + medicine + "\n")
    print("* patient data saved successfullu *")


def show_patients():
  try:
    with open (patients,"r",encoding="utf-8") as file:
      data=file.readlines()
      if not data:
        print("no pationts data")
        return
      print ( "-- patients' data --")
      for line in data:
        name,age,diagnosis,medicine=line.strip().split(",")
        print(f"name:{name}\nage:{age}\ndiagnosis:{diagnosis}\nmedicine:{medicine}")
        print("-"*15)
  except:
    print(NameError)

