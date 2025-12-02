# patient mange

# --------------------------------------
# 1-we will define function to add patient
patients="patients.txt"
def add_patient():
  name=input("enter the name : ").strip().lower()
  while True:
    age_ =input("enter the age : ").strip()
    if age_.isdigit():
      age=int(age_)
      break
    else:
       print("please enter a valid number for age")
  diagnosis =input("enter the diagnosis : ").strip().lower()
  medicine =input("enter medicin : ").strip().lower()
  with open (patients,"a",encoding="utf-8") as file:
    file.write(name + "," + str(age) + "," + diagnosis + "," + medicine + "\n")
    print("\n* patient data saved successfullu *\n")


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
  search_name=input("what's the patient's name ? ").strip().lower()
  try:
    with open (patients,"r",encoding="utf-8") as file:
      data=file.readlines()
      found=False
      print("\n-- search rusilt --\n")
      for line in data:
        name,age,diagnosis,medicine=line.strip().split(",")
        if search_name == name:
          print(f"name:{name}\nage:{age}\ndiagnosis:{diagnosis}\nmedicine:{medicine}")
          found=True
      if not found:
          print("⚠ No patient found with this name.\n")

  except FileNotFoundError:
      print("\nPatient file not found!\n")

def age_filter():
    try:
      age_limit=int(input("enter age : ").strip())
      with open (patients,"r",encoding="utf-8") as file:
         patient=file.readlines()
      patient_list=[]
      for line in patient:
         name,age,diagnosis,medicine=line.strip().split(",")
         patient_list.append({"name":name,
                              "age":int(age),
                              "diagnosis":diagnosis,
                              "medicine":medicine})
      filter_fuction=list(filter(lambda p: p['age']>=age_limit,patient_list))
      if not filter_fuction:
         print("\nno patient have this age\n")
      else:
         print("-- matching patients --")
         for p in filter_fuction:
            print (f"\nname => {p['name']}\nage => {p['age']}\ndiagnosis =>{p['diagnosis']}\nmedicine => {p['medicine']}")
            print("-"*15)
    except FileNotFoundError:
      print("NO FILE")


while True:
    print("\n__ choose option __")
    print("1 - Add Patient")
    print("2 - Show All Patients")
    print("3 - Search Patient by Name")
    print("4 - filter by age 'minimum' ")
    print("5 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        show_patients()
    elif choice == "3":
        search_patient()
    elif choice == "4":
      age_filter()
    elif choice == "5":
        print("Program closed. Goodbye ")
        break
    else:
        print("Invalid choice")
