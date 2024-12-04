class Employee:
    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept
        self.__salary = 0

    def show(self):
        print(self.name, self.__salary, self.age, self.dept)

    def get_salary(self):
        print(self.__salary)

    def set_salary(self, amount):
        if amount > 100000:
            print("Can not set any salary more than 100k")
            return
        elif amount < 50000:
            print("Can not set less than 50k")
            return 
        self.__salary = amount
        print(f"Salary is set to {amount}")

    def set_name(self, name):
        self.name = name

    def __gt__(self, other):
        return self.age > other.age
    
    def __iter__(self):
        return list(range(self.age))
    
    def __add__(self, other):
        return self.age + self.age

emp1 = Employee("Orny", 20, "Heath")
emp2 = Employee("MIclem", 25, "Tech")


