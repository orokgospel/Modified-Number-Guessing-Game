import random #To generate random numbers
name = input("Please Enter your name:\n")
print("Welcome to my Number Guessing Game,", name)

def easygame():#defined function for easy level
	number = random.randrange(1, 10)
	print(name, "I have selected a number between 1 to 10...")
	print("You have 6 chances to guess that number...")
	tries = 0
	guess = 0
	while guess !=number:
		guess=input("Guess the number:\n") #if the The number must be an integer
		try:
			guess=int(guess)
		except ValueError:
			print("The number Must be an integer!")
			continue
		tries = tries +1
		if guess>number:
			print("That was wrong")
			print("The number is less than your guessed number")
			if tries ==0:
				break
			elif tries >=6:
				print("Sorry you lost the game!!")
				break
			remaining=6-tries
			print("you have", remaining, "chances left")
		elif guess<number:
			print("That was wrong")
			print("The number is greater than your guessed number")
			if tries == 0: #Chances to the user
				break
			elif tries >= 6:
				print("GAME OVER!!!, Sorry you lost the game!")
				break
			remaining = 6 - tries
			print("you have", remaining, "chances left")
		else:
			print("You got it right, Congratulations!!!")
			print("you tried", tries ,'times')
			break
	print("The Guess Number is=", number)

def mediumgame():#defined function for Medium level
	number = random.randrange(1, 20)
	print("I have selected a number between 1 to 20...")
	print(name, "You have 4 chances to guess that number...")
	tries = 0
	guess = 0
	while guess !=number:
		guess=int(input("guess the number:\n"))
		tries = tries +1
		if guess>number:
			print("That was wrong")
			print("The number is less than your guessed number")
			if tries ==0:
				break
			elif tries >=4:
				print("Sorry you lost the game!!")
				break
			remaining=4-tries
			print("you have", remaining, "chances left\n")
		elif guess<number:
			print("That was wrong")
			print("The number is greater than your guessed number")
			if tries == 0:
				break
			elif tries >= 4:
				print("GAME OVER!!!, Sorry you lost the game!")
				break
			remaining = 4 - tries
			print("you have", remaining, "chances left\n")
		else:
			print("You got it right, Congratulations!!!")
			print("you tried", tries ,'times')
			break
	print("The Guess Number is=", number)

def hardgame():#Defined function for hard level
	number = random.randrange(1, 50)
	print("I have selected a number between 1 to 50...")
	print(name, "You have 3 chances to guess that number...")
	tries = 0
	guess = 0
	while guess !=number:
		guess=int(input("Enter number to guess:\n"))
		tries = tries +1
		if guess!=number:
			print("That was wrong")
			if tries ==0:
				break
			elif tries >=3:
				print("GAME OVER!!!, Sorry you lost the game!")
				break
			remaining=3-tries
			print("you have", remaining, "chances left")
		else:
			print("YOU GOT IT RIGHT ",name ,"Congratulations!!!")
			print("you tried", tries ,'times')
			break
	print("The Guess Number is =", number)

def game():
	global command
	command = input('Please Enter any of the letter to select your game level\n'
					'E for Easy Level\n'
					'M for Medium Level\n'
					'H for Hard level\n')
	if command == "E":
		easygame()
	elif command == "M":
		mediumgame()
	elif command == "H":
		hardgame()
	else:
		print("Game Over")
	while True:
		another_game = input("Do you wish to play again?(y/n):\n")
		if another_game == "y":
			return game()
		else:
			break
	print("\nEND OF THE GAME! Thank you for playing!")
game()