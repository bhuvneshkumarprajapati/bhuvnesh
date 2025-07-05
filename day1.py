#String formating
'''first_name = "bro"
print(f"Hello{first_name}")'''

#ineger formatting
'''age = 25
print(f"You are {age} years old")'''

#float formaatting
'''price = 10.99
print(f"the price is {price}")'''

#Boolean formatting
'''is_student = False
if(is_student):
    print("You are student")
else:
    print("you are not student")
'''

#typecasting = converting the variable from one data type to another data typ
'''age = 25
name = "yudhveer"
price = 10.99
student = True
print(type(age))
print(type(student))
print(type(price))
print(type(name))'''

#User input
'''name = input("What is your name?")
print(name)'''


#Area  of  rectangle
'''length = int(input("Enter the legth: "))
width = int(input("Enter the width: "))
area =  length * width
print(area)
print(f"The area of the rectangle is ",area)
'''

#Shopping cart Programme
'''item = input("What do you like items: ")
qty = int(input("Enter the no of items: "))
price_per_item = int(input("Enter the price: "))
total_amt = qty * price_per_item
print(total_amt)
print(f"The total amount is ",total_amt)'''

# Mad Libs Game in Python

# User se input lena
'''place = input("Koi jagah ka naam do (Place): ")
adjective = input("Ek adjective do (jaise: funny, scary, fast): ")
animal = input("Kisi jaanwar ka naam do (Animal): ")
verb_ing = input("Ek verb do jo -ing mein ho (jaise: running, dancing): ")
food = input("Koi khane ki cheez batao (Food): ")

# Final story banana
print("\n--- Tumhari Mad Libs Story ---\n")
print(f"Today I went to the {place}.")
print(f"I saw a {adjective} {animal} there.")
print(f"It was {verb_ing} and eating {food}.")
print("It looked at me and said, 'What a crazy day!' 😂")'''


#Arithmetic Operator
'''(+,-,*,/,%,**,//)
friends = 5
friends = friends + 1
print(friends)'''

'''x = 3.14
y = 4
z = 5
result = round(x)
result= abs(y)
result = pow(x,y)
result = max(x,y,z)
result = min(x,y,z)
print(result)'''

#Math function
'''import math
result = math.sqrt(16)
print(result)
print(math.pi)'''

#floor function example
'''import math
x = 9.9
print(math.floor(x))'''

#Circumference of the circle
'''import math
radius = float(input("Enter tbhe radius of the circle: "))
circumference = 2 * math.pi * radius
print(circumference)
print(f"The circumference of the ccircle is {circumference})'''


#Area of the circle 
'''import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi*radius**2
print(f"The area of the circle is {area: .2f}")'''


import math
b = float(input("Enter the base of the triangle: "))
p = float(input("Enter the perpendicular of the triangle: "))
h = math.sqrt(b**2 + p**2)
print(f"The hypotenuse of the trianle is{h: .2f}")






