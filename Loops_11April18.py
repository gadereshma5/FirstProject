
# For loop

number=[1,2,3,4,5]
for item in number:
    print(item)

name=["Nick", "Jack"]
for person in name:
    print("This person is",person)


# While loop

a=True
current=1

while a:
    if current==10:
        a=False
    else:
        print(current)
        current+=1


# While loop

a=10
while a>0:
    print("Value of a is ",a)
    a=a-1
