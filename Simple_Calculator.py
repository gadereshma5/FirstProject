# Functions


def add(x,y):
    return x+y


def sub(x,y):
    return x-y


def mult(x,y):
    return x*y


def div(x,y):
    return x/y


def print1():

 print("select operation:")
 print("1.Addition")
 print("2.Subtraction")
 print("3.Multiplication")
 print("4.Division")


print1()


choice=input("Enter choice1/2/3/4:")
num1 =int(input("Enter 1st number"))
num2 =int(input("Enter 2nd number"))
if choice == "1":
    print("Addition is:",add(num1,num2))
elif choice == "2":
    print("subtraction is:",sub(num1,num2))

elif choice == "3":
    print("Multiplication is",mult(num1,num2))

elif choice == "4":
    print("Division is",div(num1, num2))

else:
    print("Invalid input")