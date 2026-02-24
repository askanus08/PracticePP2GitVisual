class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    def total_salary(self):
        return float(base_salary)
    
class Manager(Employee):
    def __init__(self, name, base_salary, bonus_percent):
        super().__init__(name, base_salary)
        self.bonus_percent = bonus_percent
    def total_salary(self):
        return self.base_salary * (1+self.bonus_percent/100)
    
class Developer(Employee):
    def __init__(self, name, base_salary, completed_projects):
        super().__init__(name, base_salary)
        self.completed_projects = completed_projects
    def total_salary(self):
        return self.base_salary + self.completed_projects * 500

class Intern(Employee):
    pass
        
part = input().split()

if part[0] == "Manager":
    name = part[1]
    base_salary = int(part[2])
    bonus_percent = int(part[3])
    emp = Manager(name, base_salary, bonus_percent)
elif part[0] == "Developer":
    name = part[1]
    base_salary = int(part[2])
    completed_projects = int(part[3])
    emp = Developer(name, base_salary, completed_projects)
else:
    name = part[1]
    base_salary = int(part[2])
    emp = Intern(name, base_salary)

print(f"Name: {emp.name}, Total: {emp.total_salary():.2f}")