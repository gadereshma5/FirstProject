import random


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
		print("you have low health")
		break