import json
import os
from datetime import datetime


class Patient:
    """Represents a patient in the clinic system"""
    def __init__(self, name, age, phone, complaint, visit_date=None):
        self.name = name.strip()
        self.age = age
        self.phone = phone.strip()
        self.complaint = complaint.strip()
        # Use current time if no visit date is provided
        self.visit_date = visit_date if visit_date else datetime.now().strftime("%Y-%m-%d %H:%M")
        
    def to_dict(self):
        """Convert patient object to dictionary for JSON serialization"""
        return {
            "name": self.name,
            "age": self.age,
            "phone": self.phone,
            "complaint": self.complaint,
            "visit_date": self.visit_date
        }
    
    def __str__(self):
        return f"{self.name}  |  {self.age} years  |  {self.phone}  |  {self.visit_date}"


class Clinic:
    """Manages patients and handles file storage"""
    def __init__(self, json_file="patients.json"):
        self.json_file = json_file
        self.patients = self.load_patients()
    
    def load_patients(self):
        """Load patients from JSON file if it exists"""
        if not os.path.exists(self.json_file):
            return []
            
        try:
            with open(self.json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Patient(**patient_data) for patient_data in data]
        except Exception as e:
            print(f"Error reading file: {e}")
            return []
    
    def save_patients(self):
        """Save all patients to JSON file"""
        try:
            data = [patient.to_dict() for patient in self.patients]
            with open(self.json_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print("Data saved successfully ✓")
        except Exception as e:
            print(f"Error while saving: {e}")
    
    def add_patient(self):
        """Add a new patient"""
        print("\n" + "=" * 40)
        print("     Register New Patient")
        print("=" * 40)
        
        name = input("Full name: ").strip()
        
        while True:
            try:
                age = int(input("Age: "))
                if 0 < age < 120:
                    break
                print("Age should be between 1 and 120")
            except ValueError:
                print("Please enter a valid number")
                
        phone = input("Phone number: ").strip()
        complaint = input("Main complaint: ").strip()
        
        patient = Patient(name, age, phone, complaint)
        self.patients.append(patient)
        
        print("\nPatient added successfully!")
        print(patient)
        self.save_patients()
    
    def show_all_patients(self):
        """Display list of all registered patients"""
        if not self.patients:
            print("\nNo patients registered yet.")
            return
            
        print("\n" + "=" * 70)
        print(f"Total patients: {len(self.patients)}")
        print("=" * 70)
        print(f"{'Name':<25} {'Age':<6} {'Phone':<15} {'Date':<20} {'Complaint'}")
        print("-" * 90)
        
        for p in self.patients:
            print(f"{p.name:<25} {p.age:<6} {p.phone:<15} {p.visit_date:<20} {p.complaint}")
    
    def search_by_name(self):
        """Search patients by name (partial match)"""
        search_term = input("\nEnter patient name (or part of name): ").strip().lower()
        found = [p for p in self.patients if search_term in p.name.lower()]
        
        if not found:
            print("No patients found with that name.")
            return
            
        print(f"\nFound {len(found)} result(s):")
        for patient in found:
            print(patient)
    
    def menu(self):
        """Main menu loop"""
        while True:
            print("\n" + "=" * 35)
            print("       Simple Clinic System       ")
            print("=" * 35)
            print("1. Add new patient")
            print("2. Show all patients")
            print("3. Search patient by name")
            print("4. Save and exit")
            print("5. Exit without saving")
            print("=" * 35)
            
            choice = input("Choose (1-5): ").strip()
            
            if choice == "1":
                self.add_patient()
            elif choice == "2":
                self.show_all_patients()
            elif choice == "3":
                self.search_by_name()
            elif choice == "4":
                self.save_patients()
                print("\nData saved. Goodbye!")
                break
            elif choice == "5":
                print("\nExiting without saving recent changes.")
                break
            else:
                print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    clinic = Clinic()
    clinic.menu()