# Conditional Statement
# If 
'''age = int(input("Enter the age: "))
if(age>=18):
    print("You are eligieble for vote ")
else:
    print("You are not eligieble for vote")'''

#elif
'''marks = int(input("Enter the marks: "))
if(marks>90):
    print("Grade A")
elif(80<marks<90):
    print("Grade B")
elif(70<marks<80):
    print("Grade C")
elif(60<marks<70):
    print("Grade D")
else:
    print("Grade E")'''

#Calculator (Using Python)
'''operator = input("Enter the operator: ")
num1 = int(input("Enter the first no: "))
num2 = int(input("Enter the second no: "))
if(operator == "+"):
    result = num1 + num2
    print(result)
elif(operator == "-"):
    result = num1 - num2
    print(result)
elif(operator == "*"):
    result = num1 * num2
    print(result)
elif(operator == "/"):
    result = num1 / num2
    print(result)
elif(operator == "%"):
    result = num1  %  num2
    print(result)'''

#Logical Operator
#or at least one condition must be true
#and both condition must be true
#not invertible of the condition (notfalse,nottrue)

#If condition expression (using even or odd)
'''num = int(input("Enter the no: "))
if(num % 2 == 0):
    print("is even no")
else:
    print("is odd no")'''


'''name = input("Enter the name: ")
result_1 = len(name)
result_2 = name.find("h")
result_3 = name.capitalize()
result_4 = name.upper()
result_5 = name.lower()
print(result_1)
print(result_2)
print(result_3)
print(result_4)
print(result_5)'''

#Dictonary,set,list(mutable) but elements of set are immutable(string)
#Mutable(changable)
#immutable(not changable one create)

#indexing in list
'''marks = ["Apple","orange","89","litchi",56,"False"]
marks[1] = "mango"
print(marks[2])
print(marks[1])
marks.append("bnanana")
print(marks)
marks.insert(3,"pop")
print(marks)
marks.pop(3)
print(marks)'''
# pop method remove an elemnt of a list onth index no:\

#Tuples(immutable)(not changable)

'''a = (1,2,3,4,5,6,2,4,3,1,0,2,6,443,2632,2,33,223,3,4,5,6,23,4,6,46,"tisha","mango")
print(a.index(2))
print(a.count(2))
print(type(a))
print(len(a))'''


'''marks = []
m1 = input("Enter the marks name: ")
marks.append(m1)
m2 = input("Enter the marks name: ")
marks.append(m2)
m3 = input("Enter the marks name: ")
marks.append(m3)
m4 = input("Enter the marks name: ")
marks.append(m4)
m5 = input("Enter the marks name: ")
marks.append(m5)
m6 = input("Enter the marks name: ")
marks.append(m6)
m7 = input("Enter the marks name: ")
marks.append(7)
marks.sort()
print(marks)'''



