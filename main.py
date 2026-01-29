import csv
import os
import re

class EmployeeManager:
    FILE_NAME = "employees.csv"
    FIELDS = ["ID", "Name", "Position", "Salary", "Email"]

    MAX_NAME = 50
    MAX_POSITION = 30
    MAX_EMAIL = 50

    def __init__(self):
        self.employees = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.employees[str(row["ID"])] = row

    def save_data(self):
        with open(self.FILE_NAME, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.FIELDS)
            writer.writeheader()
            writer.writerows(self.employees.values())

    def _validate(self, data, is_add=True):
        if not data.get("ID"):
            return False, "ID is required"
        if not data["ID"].isdigit():
            return False, "ID must be an integer"
        if is_add and str(data["ID"]) in self.employees:
            return False, "Employee ID already exists"

        required_fields = ["Name", "Position", "Salary"]
        for key in required_fields:
            if is_add and not data.get(key):
                return False, f"{key} is required"

        if data.get("Name") and len(data["Name"]) > self.MAX_NAME:
            return False, f"Name cannot exceed {self.MAX_NAME} characters"
        
        if data.get("Position") and len(data["Position"]) > self.MAX_POSITION:
            return False, f"Position cannot exceed {self.MAX_POSITION} characters"
            
        if data.get("Email") and len(data["Email"]) > self.MAX_EMAIL:
            return False, f"Email cannot exceed {self.MAX_EMAIL} characters"

        if data.get("Salary"):
            try:
                salary = float(data["Salary"])
                if salary <= 0:
                    return False, "Salary must be positive"
            except ValueError:
                return False, "Salary must be numeric"

        email = data.get("Email", "")
        if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return False, "Invalid email format"

        return True, ""

    def add_employee(self, data):
        valid, msg = self._validate(data, is_add=True)
        if not valid:
            return False, msg

        emp_id = str(data["ID"])
        self.employees[emp_id] = data
        self.save_data()
        return True, "Employee added successfully"

    def update_employee(self, emp_id, new_data):
        emp_id = str(emp_id)
        if emp_id not in self.employees:
            return False

        valid, msg = self._validate(new_data, is_add=False)
        if not valid:
            return False

        for key, value in new_data.items():
            if value and value.strip():
                self.employees[emp_id][key] = value
        
        self.save_data()
        return True

    def delete_employee(self, emp_id):
        emp_id = str(emp_id)
        if emp_id in self.employees:
            del self.employees[emp_id]
            self.save_data()
            return True
        return False

    def search_employee(self, emp_id):
        return self.employees.get(str(emp_id))

    def get_all_employees(self):
        return list(self.employees.values())