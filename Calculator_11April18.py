import re

print("CALCULATOR")
print("Type 'quit' to exit\n")

previous = 0  # hold the result of the previously calculated equation
run= True


def perform_math():
    global run   # need to declare global variable
    global previous
    equation=""
    if previous ==0:
        equation = input("Enter Equation:")
    else:
        equation=input(str(previous))
    if equation=='quit':
        run=False
    else:
        equation=re.sub('[a-zA-Z,.:" "()]','',equation)
        if previous==0:
            previous=eval(equation)
        else:
            previous=eval(str(previous)+equation)



while run: # execute no. of statement or body till condition is true.once condition is false its coming out of the loop
    perform_math()
