from random import randint
import sys
def battle(self):
	clothing = 8
	tentacles = 8
	print("neko-chan prepares for a fight")
	print("")
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
			print("neko-chan breaks free of a tentacle")
			print("neko-chan has " + str(clothing) + " pieces of clothing left")
			print(str(tentacles) + " tentacles remain")
		elif roll1 == 0 or roll2 == 0:
			clothing = clothing - 1
			print("the tentacle monster takes a piece of neko-chan's clothing")
			print("neko-chan has " + str(clothing) + " pieces of clothing left")
			print(str(tentacles) + " tentacles remain")
		elif roll1 == 0 and roll2 == 0:
			clothing = 0
			print("the tentacle monster melts neko-chan's clothing. game over")
			break
		elif roll1 >= 1 and roll1 <= 5 and roll2 >= 1 and roll2 <= 5:
			print ("neko-chan struggles against the tentacle monster")
			print("neko-chan has " + str(clothing) + " pieces of clothing left")
			print(str(tentacles) + " tentacles remain")
		elif roll1 == 5 and roll2 == 5:
			tentacles = 0
			print("neko-chan broke free of the tentacle monster")
			break
	if clothing == 0:
		print("the tentacle monster wins")
		print("neko-chan now lives in a spooky cave with a tentacle monster")
		print("stop sucking so much")
		sys.exit()
	elif tentacles == 0:
		print("neko-chan defeated the tentacle monster")
		print("neko-chan collects her clothes and heads deeper into the cave")
		print("")

def cave(self):
	print("")
	print("this cave looks to be about 10 rooms long")
	print("neko-chan is in room " + str(currentroom) + " of 10")
	print("")

def advance(self):
	print("")
	raw_input("press enter to continue")
	print("")

#endmethods
#beginmain

print("")
print("neko-chan has gotten separated from her senpais on a school trip")
advance(0)
print("night falls and neko-chan takes refuge in a cave to avoid the weeaboos")
advance(0)
print("little does she know, something only slightly better than weeaboos lurks within")
advance(0)
print("")
print("")
print("KAWAIIDESUKA PRESENTS")
print("")
print("")
print("")
print("SUPER HENTAI BATTLE SIM CURRENT YEAR II")
print("")
print("")
print("")
raw_input("press enter for tentacled fun")
currentroom = 1
while currentroom != 10:
	encounter = randint(0,1)	
	cave(0)
	if encounter == 1:
		battle(0)
	raw_input("press enter to carry on")
	currentroom = currentroom + 1

cave(0)
print("neko-chan reaches the end of the cave")
advance(0)
print("she looks back and sees many crushed tentacles")
advance(0)
print("neko-chan smiles and makes some tea")
advance(0)
print("neko-chan waits for the sun to rise")
advance(0)
print("as the sun rises, she leaves the cave")
advance(0)
print("she sees dozens of weeaboos who failed to get inside")
advance(0)
print("they are all on fire as the sun burns their snow-white skin")
advance(0)
print("neko-chan continues on to her school to reunite with her senpais")
advance(0)
print("her senpais ask if she is ok")
advance(0)
print("neko-chan puts on sunglasses and smiles at them")
advance(0)
print("neko-chan continues walking to class, ignoring her senpais")
advance(0)
print("former senpais that is")
advance(0)
print("because neko-chan has graduated")
advance(0)
print("graduated from the school of badassery")
advance(0)
print("everything explodes in the background and an eagle screeches overhead")
advance(0)
print("neko-chan hums the star spangled banner")
advance(0)
print("neko-chan is a true american hero")
advance(0)
print("A KAWAIIDESUKA GAME")
advance(0)
print("WHY THE HELL DID YOU FINISH THIS")
advance(0)
print("SERIOUSLY WHAT IS WRONG WITH YOU")
print("")
