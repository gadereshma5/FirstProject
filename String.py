#  String Manupulation(Sring is any text that you want to be Treated as a text within a programm)
print("H"+"e"+"l"+"l"+"o")
print("This cost's "+str(6)+" dollars")
print("this cost's "+str(6+5)+" dollars")

#  String Splits
print("Hello:Nick")
print(("Hello:Nick").split(":"))
print(("Hello.Reshma").split("."))
print(("Hello,Reshma").split(","))

print("My name is "+("Reshma:Hello:World").split(":")[0])

print("Message is "+("Reshma:Hello:World").split(":")[1])
print("My name is "+["Reshma","Hello","World"][0])