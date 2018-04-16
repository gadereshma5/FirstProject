import random


class Enemy:   # Syntax:  class Class_name:
	atklow=60
	atkhigh=80

	def getAtk(self):      # Function

		print(self.atklow)


enemy1=Enemy()      # Object1
enemy1.getAtk()

enemy2=Enemy()      # Object2
enemy2.getAtk()

playerhp=260
enemyatklow=60
enemyatkhigh=80

while playerhp>0:
	dmg=random.randrange(enemyatklow,enemyatkhigh)
	playerhp=playerhp-dmg
	if playerhp<=30:
		playerhp=30
	print("enemy striks for",dmg,"Point of damage. Current HP",playerhp)

	if playerhp>30:
		continue

	print("you have low health")
	break