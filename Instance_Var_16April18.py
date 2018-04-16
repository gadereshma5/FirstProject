'''
Types of comments
1.Multi-line-uses '''    '''
2.Single line-uses #......

Multi-lines comment:
Class
objects
instance variable
'''
# Single line comments:


import random


class Enemy:   # Syntax:  class Class_name:

	HP=200

	def __init__(self,atklow,atkhigh):   # instance variables

		self.atklow=atklow
		self.atkhigh=atkhigh

	def getAtk(self):      # Function

		print("attack is ",self.atklow)

	def getHP(self):
		print("HP is", self.HP)


enemy1=Enemy(40,70)      # Object1 and passed the instance variable values
enemy1.getAtk()
enemy1.getHP()

enemy2=Enemy(45,75)      # Object2
enemy2.getAtk()
enemy2.getHP()



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