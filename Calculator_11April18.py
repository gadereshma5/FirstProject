import re

print("CALCULATOR")
print("Type 'quit' to exit\n")

previous = 0  # hold the result of the previously calculated equation
run= True


def perform_math():
    global run   # need to declare global variable
    global previous

    equation = input("Enter Equation:")
    if equation=='quit':
        run=False
    else:
        print("You typed....",equation)



while run: # execute no. of statement or body till condition is true.once condition is false its coming out of the loop
    perform_math()
