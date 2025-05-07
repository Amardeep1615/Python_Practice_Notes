class Employee:
    def __init__(self, id, name, role, salary):
        self.id = id
        self.name = name
        self.role = role
        self.salary = salary

    def get_details(self):
        print(f"ID: {self.id}, Name: {self.name}, Role: {self.role}, Salary: {self.salary}")

    def get_access_level(self):
        print("Access Level: General Access")


class Developer(Employee):
    def __init__(self, id, name, salary, programming_language):
        self.id = id
        self.name = name
        self.role = "Developer"
        self.salary = salary
        self.programming_language = programming_language

    def get_access_level(self):
        print("Access Level: Code Repository Access")

    def get_details(self):
        print(f"ID: {self.id}, Name: {self.name}, Role: {self.role}, Salary: {self.salary}")
        print(f"Language: {self.programming_language}")


class Tester(Employee):
    def __init__(self, id, name, salary, testing_tool):
        self.id = id
        self.name = name
        self.role = "Tester"
        self.salary = salary
        self.testing_tool = testing_tool

    def get_access_level(self):
        print("Access Level: Test Management Tool Access")

    def get_details(self):
        print(f"ID: {self.id}, Name: {self.name}, Role: {self.role}, Salary: {self.salary}")
        print(f"Tool: {self.testing_tool}")


class Manager(Employee):
    def __init__(self, id, name, salary, team_size):
        self.id = id
        self.name = name
        self.role = "Manager"
        self.salary = salary
        self.team_size = team_size

    def get_access_level(self):
        print("Access Level: Admin Dashboard Access")

    def get_details(self):
        print(f"ID: {self.id}, Name: {self.name}, Role: {self.role}, Salary: {self.salary}")
        print(f"Team Size: {self.team_size}")


def display_employee_info(employee):
    employee.get_access_level()
    employee.get_details()
    print()


# Example usage
employees = [
    Developer(101, "Alice", 75000, "Python"),
    Tester(102, "Bob", 60000, "Selenium"),
    Manager(103, "Charlie", 90000, 10),
    Employee(104, "Diana", "Employee", 50000)
]

for emp in employees:
    display_employee_info(emp)



