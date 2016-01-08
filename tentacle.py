from random import randint
clothing = 8
tentacles = 8
while clothing >= 0 or tentacles >= 0:
	print("--------------------")
	raw_input("press enter to roll")
	print("--------------------")
	roll1 = randint(0,5)
	roll2 = randint(0,5)
	print(roll1)
	print(roll2)
	if roll1 >= 1 and roll1 <= 5 and roll2 >= 1 and roll2 <= 5:
		print ("you struggle against the tentacle monster")
	elif roll1 == 0 and roll2 == 0:
		clothing = 0
		print("the tentacle monster melts your clothing. game over")
	elif roll1 == 0 or roll2 == 0:
		clothing = clothing - 1
		print("the tentacle monster takes a piece of your clothing")
		print("you have " + str(clothing) + " pieces of clothing left")
	elif roll1 == 5 or roll2 == 5:
		tentacles = tentacles - 1
		print("you break free of a tentacle")
		print(str(tentacles) + " tentacles remain")
	elif roll1 == 5 and roll2 == 5:
		tentacles = 0
		print("you broke free of the tentacle monster")
