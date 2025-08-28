'''class student:
    def __init__(self, name):
        self.name =  name
s1 = student("raju")
print(s1.name)
del s1.name
print(s1.name)  '''


'''
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass
acc1 = Account(12345, "password123")
print(acc1.acc_no)
print(acc1.acc_pass)
'''

'''class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def show_details(self):
        print("The complex number is {}i + {}i".format(self.real,self.imaginary))
    def add(self,num2):
        new_real = self.real + num2.real
        new_imaginary = self.imaginary + num2.imaginary
        return ComplexNumber(new_real, new_imaginary)
num1 = ComplexNumber(3, 4)
num1.show_details()
num2 = ComplexNumber(5, 6)
num2.show_details()
result = num1.add(num2)
print("The result of addition is {}i + {}i".format(result.real, result.imaginary))'''


'''Example: Create a class named employee with instance variables name and designation.'''

'''class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def peremeter(self):
        return 2 * 3.14 * self.radius
c1 = Circle(5)
print(c1.area())
print(c1.peremeter())'''


'''class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department  
        self.salary = salary
    def show_details(self):
        print("Role: {}, Department: {}, Salary: {}".format(self.role, self.department, self.salary))
class Manager(Employee):
    def __init__(self, name , age):
        self.name = name
        self.age = age
        super().__init__("Manager", "Management", 80000)
    def show_details(self):
        print("Name: {}, Age: {}, Role: {}, Department: {}, Salary: {}".format(self.name, self.age, self.role, self.department, self.salary))
eng1 = Manager("Alice", 35)
eng1.show_details()'''



'''Example: Create a class named student with instance variables first, second and result (addition of first and second).'''
'''
# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Derived class (Inheritance)
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    # Polymorphism - method overriding
    def show_details(self):
        print(f"Student Name: {self.name}, Age: {self.age}, ID: {self.student_id}")

# Another derived class
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show_details(self):
        print(f"Teacher Name: {self.name}, Age: {self.age}, Subject: {self.subject}")

# Creating objects
student1 = Student("Amit", 16, "S101")
teacher1 = Teacher("Mrs. Sharma", 35, "Maths")

# Accessing methods
student1.show_details()
teacher1.show_details()
'''



