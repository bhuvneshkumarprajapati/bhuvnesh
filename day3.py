'''class person:
    def __init__(self, name, age, gender):
        self.name  = name
        self.age = age
        self.gender = gender

    def display(self):
        print("the name {}, age is {} and gender is {}".format(self.name, self.age, self.gender))

p1 = person("poorvi", 18, "female")
p1.display()
'''


'''Example: Create a class name Employee with
i. a class variable office_name, and
ii. instance variables name and designation.
iii. Create a show_detail() method'''

'''class employee:
    ofiice_name = "Tech solutions"
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
    def show_details(self):
        print("the name is {} and designation is {}".format(self.name,self.designation))
e1 = employee("raju","engineer")
e1.show_details()'''


'''Example: Program modifying mutable type attributes.'''

'''class number:
    evens = []
    odds = []
    def __init__(self,num):
        self.num = num
        if num%2 == 0:
            number.evens.append(num)
        else:
            number.odds.append(num)
N1 = number(23)
N2 = number(26)
N3 = number(24)
N4 = number(29)
N5 = number(24)
N6 = number(27)
print("the even numbers are",number.evens)
print("the odd numbers are",number.odds)
'''
'''
class MathOperations:
    @staticmethod
    def add_number(a, b):
        return a + b
    @staticmethod
    def subtract_number(a, b):
        return a - b
object = MathOperations()
result_add = MathOperations.add_number(10, 5)
result_subtract = MathOperations.subtract_number(10, 5)
print("Addition Result:", result_add)
print("Subtraction Result:", result_subtract)'''



'''Example: Create a class named student with instance variables first, second and result (addition of first and second).'''


'''
class student:
    first = 0
    second = 0
    result = 0
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def display(self):
        print("the first number is {} and second number is {}".format(self.first, self.second))
        print("addition of two num is {}".format(self.result))
    def calculate(self):
        self.result = self.first + self.second
obj = student(10,20)
obj.calculate()
obj.display()'''


