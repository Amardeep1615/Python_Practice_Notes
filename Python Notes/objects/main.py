class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.role = "Employee"

    def get_details(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Role: {self.role}, Salary: {self.salary}"

    def get_access_level(self):
        return "General Access"


# Subclass: Developer
class Developer(Employee):
    def __init__(self, emp_id, name, salary, programming_language):
        super().__init__(emp_id, name, salary)
        self.programming_language = programming_language
        self.role = "Developer"

    def get_access_level(self):
        return "Code Repository Access"

    def get_details(self):
        base = super().get_details()
        return f"{base}, Language: {self.programming_language}"


# Subclass: Tester
class Tester(Employee):
    def __init__(self, emp_id, name, salary, test_tool):
        super().__init__(emp_id, name, salary)
        self.test_tool = test_tool
        self.role = "Tester"

    def get_access_level(self):
        return "Test Management Tool Access"

    def get_details(self):
        base = super().get_details()
        return f"{base}, Tool: {self.test_tool}"


# Subclass: Manager
class Manager(Employee):
    def __init__(self, emp_id, name, salary, team_size):
        super().__init__(emp_id, name, salary)
        self.team_size = team_size
        self.role = "Manager"

    def get_access_level(self):
        return "Admin Dashboard Access"

    def get_details(self):
        base = super().get_details()
        return f"{base}, Team Size: {self.team_size}"


# Example usage
def display_employee_info(employee):
    print(employee.get_details())
    print("Access Level:", employee.get_access_level())
    print("-" * 40)


# Records
employees = [
    Developer(101, "Alice", 75000, "Python"),
    Tester(102, "Bob", 60000, "Selenium"),
    Manager(103, "Charlie", 90000, 10),
    Employee(104, "Diana", 50000)
]

# Polymorphic behavior
for emp in employees:
    display_employee_info(emp)

