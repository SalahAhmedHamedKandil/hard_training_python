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

def search_patient():
  search_name=input("what's the patient's name ? ")
  try:
    with open (patients,"r",encoding="utf-8") as file:
      data=file.readlines()
      found=False
      print("search rusilt")
      for line in data:
        name,age,diagnosis,medicine=line.strip().split(",")
        if search_name == name:
          print(f"name:{name}\nage:{age}\ndiagnosis:{diagnosis}\nmedicine:{medicine}")
          found=True
      if not found:
          print("⚠ No patient found with this name.\n")

  except FileNotFoundError:
      print("\nPatient file not found!\n")


while True:
    print("\n__ choose option __")
    print("1 - Add Patient")
    print("2 - Show All Patients")
    print("3 - Search Patient by Name")
    print("5 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        show_patients()
    elif choice == "3":
        search_patient()
    elif choice == "5":
        print("Program closed. Goodbye ")
        break
    else:
        print("Invalid choice")
