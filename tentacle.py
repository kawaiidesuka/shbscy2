from random import randint
import sys
import os
def getVoice(x):
    print (x);
    try:
        return (os.system("espeak -s 160 -v en+f4 '" + x + "'"));
    except:
        return (print("Voice is offline"));
def battle(self):
	clothing = 8
	tentacles = 8
	getVoice("neko-chan prepares for a fight")
	print("")
	input("press enter to fight the tentacle monster")
	while clothing > 0:
		if tentacles == 0:
			break
		print("--------------------")
		input("press enter to roll")
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
			getVoice("neko-chan breaks free of a tentacle")
			print("neko-chan has " + str(clothing) + " pieces of clothing left")
			print(str(tentacles) + " tentacles remain")
		elif roll1 == 0 or roll2 == 0:
			clothing = clothing - 1
			getVoice("the tentacle monster takes a piece of neko-chans clothing")
			print("neko-chan has " + str(clothing) + " pieces of clothing left")
			print(str(tentacles) + " tentacles remain")
		elif roll1 == 0 and roll2 == 0:
			clothing = 0
			getVoice("the tentacle monster melts neko-chan's clothing. game over")
			break
		elif roll1 >= 1 and roll1 <= 5 and roll2 >= 1 and roll2 <= 5:
			getVoice("neko-chan struggles against the tentacle monster")
			print("neko-chan has " + str(clothing) + " pieces of clothing left")
			print(str(tentacles) + " tentacles remain")
		elif roll1 == 5 and roll2 == 5:
			tentacles = 0
			getVoice("neko-chan broke free of the tentacle monster")
			break
	if clothing == 0:
		getVoice("the tentacle monster wins")
		getVoice("neko-chan now lives in a spooky cave with a tentacle monster")
		getVoice("stop sucking so much")
		sys.exit()
	elif tentacles == 0:
		getVoice("neko-chan defeated the tentacle monster")
		getVoice("neko-chan collects her clothes and heads deeper into the cave")
		print("")

def cave(self):
	print("")
	print("this cave looks to be about 10 rooms long")
	print("neko-chan is in room " + str(currentroom) + " of 10")
	print("")

def advance(self):
	print("")
	input("press enter to continue")
	print("")

#endmethods
#beginmain

print("")
getVoice("neko-chan has gotten separated from her senpais on a school trip")
advance(0)
getVoice("night falls and neko-chan takes refuge in a cave to avoid the weeaboos")
advance(0)
getVoice("little does she know, something only slightly better than weeaboos lurks within")
advance(0)
print("")
print("")
getVoice("KAWAIIDESUKA PRESENTS")
print("")
print("")
print("")
getVoice("SUPER HENTAI BATTLE SIM CURRENT YEAR 2")
print("")
print("")
print("")
input("press enter for tentacled fun")
currentroom = 1
while currentroom != 10:
	encounter = randint(0,1)	
	cave(0)
	if encounter == 1:
		battle(0)
	input("press enter to carry on")
	currentroom = currentroom + 1

cave(0)
getVoice("neko-chan reaches the end of the cave")
advance(0)
getVoice("she looks back and sees many crushed tentacles")
advance(0)
getVoice("neko-chan smiles and makes some tea")
advance(0)
getVoice("neko-chan waits for the sun to rise")
advance(0)
getVoice("as the sun rises, she leaves the cave")
advance(0)
getVoice("she sees dozens of weeaboos who failed to get inside")
advance(0)
getVoice("they are all on fire as the sun burns their snow-white skin")
advance(0)
getVoice("neko-chan continues on to her school to reunite with her senpais")
advance(0)
getVoice("her senpais ask if she is ok")
advance(0)
getVoice("neko-chan puts on sunglasses and smiles at them")
advance(0)
getVoice("neko-chan continues walking to class, ignoring her senpais")
advance(0)
getVoice("former senpais that is")
advance(0)
getVoice("because neko-chan has graduated")
advance(0)
getVoice("graduated from the school of badassery")
advance(0)
getVoice("everything explodes in the background and an eagle screeches overhead")
advance(0)
getVoice("neko-chan hums the star spangled banner")
advance(0)
getVoice("neko-chan is a true american hero")
advance(0)
getVoice("A KAWAIIDESUKA GAME")
advance(0)
getVoice("WHY THE HELL DID YOU FINISH THIS")
advance(0)
getVoice("SERIOUSLY WHAT IS WRONG WITH YOU")
print("")
