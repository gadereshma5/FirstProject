# Infinite argument


def fun(*people):
    for person in people:  # Syntax: for <variable> in <sequence>:
        print("This person is",person)


fun("Nick","Jack","Jimmy")
