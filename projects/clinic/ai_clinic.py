patients_file = "patients.txt"

def add_patient():
    name = input("Enter the name: ").strip().lower()
    while True:
        age_input = input("Enter the age: ").strip()
        if age_input.isdigit():
            age = int(age_input)
            break
        else:
            print("Please enter a valid number for age.")
    diagnosis = input("Enter the diagnosis: ").strip().lower()
    medicine = input("Enter medicine: ").strip().lower()

    with open(patients_file, "a", encoding="utf-8") as file:
        file.write(f"{name},{age},{diagnosis},{medicine}\n")
    print("\n* Patient data saved successfully *\n")

def show_patients():
    try:
        with open(patients_file, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if not lines:
                print("No patient data available.")
                return
            print("\n-- Patients' Data --")
            for index, line in enumerate(lines, start=1):
                try:
                    name, age, diagnosis, medicine = line.strip().split(",")
                    print(f"{index}. Name: {name}")
                    print(f"   Age: {age}")
                    print(f"   Diagnosis: {diagnosis}")
                    print(f"   Medicine: {medicine}")
                    print("-" * 30)
                except ValueError:
                    print(f"Warning: Found improperly formatted patient data at line {index}, skipping.")
    except FileNotFoundError:
        print("No patient records found.")

def search_patient():
    search_name = input("What's the patient's name? ").strip().lower()
    try:
        with open(patients_file, "r", encoding="utf-8") as file:
            lines = file.readlines()
            found = False
            print("\n-- Search Results --\n")
            for index, line in enumerate(lines, start=1):
                try:
                    name, age, diagnosis, medicine = line.strip().split(",")
                    if name == search_name:
                        print(f"{index}. Name: {name}")
                        print(f"   Age: {age}")
                        print(f"   Diagnosis: {diagnosis}")
                        print(f"   Medicine: {medicine}")
                        print("-" * 30)
                        found = True
                except ValueError:
                    continue
            if not found:
                print("⚠ No patient found with this name.\n")
    except FileNotFoundError:
        print("Patient file not found!")

def age_filter():
    try:
        age_limit_input = input("Enter minimum age: ").strip()
        if not age_limit_input.isdigit():
            print("Please enter a valid number for age.")
            return
        age_limit = int(age_limit_input)

        with open(patients_file, "r", encoding="utf-8") as file:
            lines = file.readlines()

        patients_list = []
        for line in lines:
            try:
                name, age, diagnosis, medicine = line.strip().split(",")
                patients_list.append({
                    "name": name,
                    "age": int(age),
                    "diagnosis": diagnosis,
                    "medicine": medicine
                })
            except ValueError:
                continue

        filtered = list(filter(lambda p: p['age'] >= age_limit, patients_list))

        if not filtered:
            print("\nNo patients found with the specified minimum age.\n")
        else:
            print("\n-- Matching Patients --")
            for index, p in enumerate(filtered, start=1):
                print(f"{index}. Name: {p['name']}")
                print(f"   Age: {p['age']}")
                print(f"   Diagnosis: {p['diagnosis']}")
                print(f"   Medicine: {p['medicine']}")
                print("-" * 30)

    except FileNotFoundError:
        print("No patient records found.")

def main_menu():
    while True:
        print("\n__ Choose option __")
        print("1 - Add Patient")
        print("2 - Show All Patients")
        print("3 - Search Patient by Name")
        print("4 - Filter by Age (minimum)")
        print("5 - Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_patient()
        elif choice == "2":
            show_patients()
        elif choice == "3":
            search_patient()
        elif choice == "4":
            age_filter()
        elif choice == "5":
            print("Program closed. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
