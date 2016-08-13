import random
def roll_the_dice():
	max=8
	min=1
	roll_dice="yes"
	while roll_dice =="yes" or roll_dice=="y":
		print("rolling the dice...")
		print("The values are...")
		print random.randint(min,max)
		print random.randint(min,max)

	roll_dice=raw_input("roll the dices again?")


roll_the_dice()