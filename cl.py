car = {"make": "Toyota", "model": "Sonta", "speed": 0, "speed_factor": 1, "started": False}
car1 = {"make": "Toyota", "model": "Sonta"}

def display_props(car):
    # get and display the car properties
    try:
        make = car['make']
        model = car['model']
        speed = car['speed']
    except:
        print("something went wrong")
        return

    print(f"Make: {make}, Model: {model}, Speed: {speed}")

def accelerate(car, speed_factor=1):
    car["speed"] += speed_factor

def start(car):
    car["started"] = True

    
display_props(car)
display_props(car1)

# class Person:
#     fname = ""
#     lname = ""
#     password = ""
#     username = ""
#     dob = ""
#     pob = ""

# class Admin(Person):
#     address = ""
#     married = ""

    
    

# class Teacher(Person):
#     pass


# class Student(Person):
    
    
#     def generate_report(data):
#         pass

# std = Student

# std.generate_report(data="")

# string = "miclem"

# string.capitalize()

class Mamal:
    name = "Mamal"
    age = 0
    legs = 4
    sex = "M"

    def talk(self):
        print("mamal can't talk yet")

    def walk():
        print("mamal can't work yet")

    def descripe_mamal(self):
        print(f"{self.name}, {self.age}, {self.legs}, {self.sex}")

class Dog(Mamal):
    name = "Bingo"
    age = 0.5

    def talk(self):
        print(f"{self.name} is barging...")


dog = Dog()
dog1 = Dog()
dog1.name = "Bazu"
dog.descripe_mamal()
dog1.descripe_mamal()


