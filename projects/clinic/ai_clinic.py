# Patient Management System (Add - Show - Filter by Age)

def add_patient():
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    diagnosis = input("Enter diagnosis: ")
    medicine = input("Enter medicine: ")

    with open("patients.txt", "a", encoding="utf-8") as file:
        file.write(name + "," + age + "," + diagnosis + "," + medicine + "\n")

    print("\n✅ Patient data saved successfully!\n")


def show_patients():
    try:
        with open("patients.txt", "r", encoding="utf-8") as file:
            data = file.readlines()

            if not data:
                print("\n⚠ No patient data found.\n")
                return

            print("\n📋 All Patients:\n")
            for line in data:
                name, age, diagnosis, medicine = line.strip().split(",")
                print(f"Name: {name} | Age: {age} | Diagnosis: {diagnosis} | Medicine: {medicine}")

    except FileNotFoundError:
        print("\n⚠ Patient file not found!\n")


# ✅ Filter patients by age using filter()
def filter_by_age():
    try:
        age_limit = int(input("Enter minimum age to search: "))

        with open("patients.txt", "r", encoding="utf-8") as file:
            patients = file.readlines()

        patients_list = []
        for line in patients:
            name, age, diagnosis, medicine = line.strip().split(",")
            patients_list.append({
                "name": name,
                "age": int(age),
                "diagnosis": diagnosis,
                "medicine": medicine
            })

        filtered = list(filter(lambda p: p["age"] >= age_limit, patients_list))

        if not filtered:
            print("\n⚠ No patients found with this age or above.\n")
        else:
            print("\n✅ Matching Patients:\n")
            for p in filtered:
                print(f"Name: {p['name']} | Age: {p['age']} | Diagnosis: {p['diagnosis']} | Medicine: {p['medicine']}")

    except FileNotFoundError:
        print("\n⚠ Patient file does not exist.\n")
    except ValueError:
        print("\n⚠ Please enter a valid age number.\n")


# ✅ Main Menu
while True:
    print("\n1 - Add Patient")
    print("2 - Show All Patients")
    print("3 - Filter Patients by Age")
    print("4 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        show_patients()
    elif choice == "3":
        filter_by_age()
    elif choice == "4":
        print("Program closed. Goodbye 👋")
        break
    else:
        print("Invalid choice ❌")
