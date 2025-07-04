'''num = int(input("Enter the no: "))
if(num==0):
    fact=1
fact=1
for i in range(1,num+1):
    fact = fact*i
print("Factorial of the number is: ",fact)'''

'''year = int(input("Enter the year: "))
if(year%4==0 or year%100!=0 and year%400==0):
    print("is the leap year")
else:
    print("is not a leap year")'''


'''num1 = int(input("Enter the first no: "))
num2 = int(input("Enter the second  no: "))
num3 = int(input("Enter the thirfd no: "))
if(num1>num2 and num1>num3):
    print("num1 is greater")
elif(num2>num3 and num2>num1):
    print("num2 is greater")
else:
    print("num3 is greater")'''

'''import random
num = random.randint(1,1000)
print(num)'''

'''num = int(input("Enter the no: "))
if(num>0):
    print("is the positive number")
elif(num==0):
    print("number is equal to zero")
else:
    print("is the negative number")
'''

'''num = int(input("Enter the no: "))
if(num%2==0):
    print("is even number")
else:
    print("is the odd number")'''

'''n = int(input("Enter the no: "))
for i in range(1,11):
    print(n,"x",i,"=",n*i)
    '''


'''n = int(input("Enter the no: "))
i=1
while(i<=10):
    print(n,"x",i,"=",n*i)
    i+=1'''

'''a=0
b=1
num=int(input("Enter the no: "))
for i in range(1,num+1):
    c=a+b
    a=b
    b=c
    print(c)'''

'''i=1
while(i<=10):
    print(i)
    i+=1'''

'''for i in range(1,11):
    print(i)'''

'''for i in range(1,7):
    for j in range(1,i+1):
        print("*", end=" ")
    print()'''

'''rows=5
num = 1
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1'''

'''rows=5
for i in range(1,rows+1):
    for j in range(65,65+i):
        print(chr(j),end=" ")
    print()'''

'''rows=int(input("Enter the rows: "))
for  i in range(rows,0,-1):
    print("*" * i)'''

