from random import randint
clothing = 8
tentacles = 8
print("you are a schoolgirl in a spooky cave")
print("you hear slithering in the darkness")
print("you think this is perfectly fine")
print("because this game would not exist without some sort of story")
print("you continue into the cave")
print("a slippery tentacle grabs your leg")
print("you wish you had brought hot tea to spill on it")
print("you prepare for a fight")
print("you wish you were not a moe character")
raw_input("press enter to fight the tentacle monster")
while clothing > 0:
	if tentacles == 0:
		break
	print("--------------------")
	raw_input("press enter to roll")
	print("--------------------")
	roll1 = randint(0,5)
	roll2 = randint(0,5)
	#debug
		#print(roll1)
		#print(roll2)
		#print(tentacles)
		#print(clothing)
	#enddebug
	if roll1 == 5 or roll2 == 5:
		tentacles = tentacles - 1
		print("you break free of a tentacle")
		print(str(tentacles) + " tentacles remain")
	elif roll1 == 0 or roll2 == 0:
		clothing = clothing - 1
		print("the tentacle monster takes a piece of your clothing")
		print("you have " + str(clothing) + " pieces of clothing left")
	elif roll1 == 0 and roll2 == 0:
		clothing = 0
		print("the tentacle monster melts your clothing. game over")
		break
	elif roll1 >= 1 and roll1 <= 5 and roll2 >= 1 and roll2 <= 5:
		print ("you struggle against the tentacle monster")
	elif roll1 == 5 and roll2 == 5:
		tentacles = 0
		print("you broke free of the tentacle monster")
		break
if clothing == 0:
	print("the tentacle monster wins")
	print("you now live in a spooky cave with a tentacle monster")
	print("stop sucking so much")
elif tentacles == 0:
	print("you defeated the tentacle monster")
	print("you return to school and your senpais hug you")
	print("but out of the corners of your eyes")
	print("you occasionally see purple things slithering")
