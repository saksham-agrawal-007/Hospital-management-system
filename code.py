# hospital_management_extended.py

# ... (rest of the code remains unchanged)

class Patient:
    def _init_(self, patient_id, name, age, gender, illness):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.illness = illness

    def _str_(self):
        return f"[P{self.patient_id}] {self.name}, {self.age} y/o, {self.gender}, Illness: {self.illness}"

class Doctor:
    def _init_(self, doctor_id, name, specialization, phone, available):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.phone = phone
        self.available = available

    def _str_(self):
        return f"[D{self.doctor_id}] Dr. {self.name}, Specialization: {self.specialization}, Phone: {self.phone}, Available: {self.available}"

class Hospital:
    def _init_(self):
        self.patients = {}
        self.doctors = {}
        self.patient_counter = 1
        self.doctor_counter = 1

    # Patient Methods
    def add_patient(self, name, age, gender, illness):
        patient = Patient(self.patient_counter, name, age, gender, illness)
        self.patients[self.patient_counter] = patient
        print(f"Patient added with ID: P{self.patient_counter}")
        self.patient_counter += 1

    def view_patients(self):
        if not self.patients:
            print("No patients found.")
        for patient in self.patients.values():
            print(patient)

    def search_patient(self, patient_id):
        patient = self.patients.get(patient_id)
        if patient:
            print("Patient found:")
            print(patient)
        else:
            print("Patient not found.")

    def discharge_patient(self, patient_id):
        if patient_id in self.patients:
            del self.patients[patient_id]
            print(f"Patient ID P{patient_id} discharged.")
        else:
            print("Patient ID not found.")

    # Doctor Methods
    def add_doctor(self, name, specialization, phone, available):
        doctor = Doctor(self.doctor_counter, name, specialization, phone, available)
        self.doctors[self.doctor_counter] = doctor
        print(f"Doctor added with ID: D{self.doctor_counter}")
        self.doctor_counter += 1

    def view_doctors(self):
        if not self.doctors:
            print("No doctors found.")
        for doctor in self.doctors.values():
            print(doctor)

    def search_doctor(self, doctor_id):
        doctor = self.doctors.get(doctor_id)
        if doctor:
            print("Doctor found:")
            print(doctor)
        else:
            print("Doctor not found.")

def main():
    hospital = Hospital()

    while True:
        print("\n=== Hospital Management System ===")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Search Patient by ID")
        print("4. Discharge Patient")
        print("5. Add Doctor")
        print("6. View All Doctors")
        print("7. Search Doctor by ID")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = input("Enter age: ")
            gender = input("Enter gender: ")
            illness = input("Enter illness: ")
            hospital.add_patient(name, age, gender, illness)
        elif choice == "2":
            hospital.view_patients()
        elif choice == "3":
            pid = int(input("Enter patient ID (numeric): "))
            hospital.search_patient(pid)
        elif choice == "4":
            pid = int(input("Enter patient ID (numeric): "))
            hospital.discharge_patient(pid)
        elif choice == "5":
            name = input("Enter doctor's name: ")
            specialization = input("Enter specialization: ")
            phone = input("Enter phone number: ")
            available = input("Is the doctor available (Yes/No)? ")
            hospital.add_doctor(name, specialization, phone, available)
        elif choice == "6":
            hospital.view_doctors()
        elif choice == "7":
            did = int(input("Enter doctor ID (numeric): "))
            hospital.search_doctor(did)
        elif choice == "8":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "_main_": # Changed _name_ to __name__
    main()
