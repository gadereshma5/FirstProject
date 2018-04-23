from random import shuffle
import random
print(random.randint(0,5))

mylist=[2,10,"Reshma",True]
print(random.choice(mylist))

print(random.random()*100)

for a in range(3):
	print(random.randrange(0,10,2))
#####################################
x=[[i]for i in range(10)]
shuffle(x)
print(x)
# print x  gives  [[9], [2], [7], [0], [4], [5], [3], [1], [8], [6]]
# of course your results will vary
# Note that shuffle works in place, and returns None.
