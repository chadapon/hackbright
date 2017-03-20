import random

# magic_number = (int(random.randint(1,10)))

#game_level = int(raw_input("What's game level you want today? 1-easy, 2-medium, 3-challenge! "))

#print game_level

#print type(game_level)

# def print_rule(game_level):
# 	print (game_level)
# 	if game_level == 1:
# 		print ('the magic game will radom pick the number from 1 to 100')
# 		print ('you have 7 times to guess what number it is!')
# 		print ('Good luck! start pick your number!')
# 	elif game_level == 2:
# 		print ('the magic game will radom pick the number from -100 to 100')
# 		print ('you have 7 times to guess what number it is!')
# 		print ('Good luck! start pick your number!')
# 	else:
# 		print ('the magic game will radom pick the number from -100 to 100')
# 		print ('you have 5 times to guess what number it is!')
# 		print ('Good luck! start pick your number!')

def print_rule(game_level):
    print (game_level)
    if game_level == 1:
        num_guesses_allowed = 7
    elif game_level == 2:
       num_guesses_allowed = 6
    else:
       num_guesses_allowed = 5
    print ('the magic game will random pick the number from 0 to 100')
    print ('you have'), num_guesses_allowed ,('times to guess what number it is!')
    print ('Good luck! start pick your number!')
    return num_guesses_allowed


def main():
	game_level = int(input("What's game level you want today? 1-easy, 2-soso, 3-hard!, 0-Exit the game "))
	print (game_level)
	num_guesses_allowed = print_rule(game_level)
	magic_number1 = (int(random.randint(1,100)))
	magic_number2 = (int(random.randint(-100,100)))
	magic_number3 = (int(random.randint(-100,200)))
	if game_level == 1:
		print ('We will start with level', game_level)
		counting_game(num_guesses_allowed, magic_number1)
	elif game_level == 2:
		print ('We will start with level', game_level)
		counting_game(num_guesses_allowed, magic_number2)
	elif game_level == 3:
		print ('We will start with level', game_level)
		counting_game(num_guesses_allowed, magic_number3)
	elif game_level == 0:
		print ('You exit the game!')
		return
	else:
		print ("Bye Bye!")	


	
def counting_game(num_guesses_allowed,magic_number):
	counter = 0
	number_guess = []
	while counter < num_guesses_allowed:
		str_number_guess = []
		for numb in number_guess:
			str_number_guess.append(str(numb))
		if len(number_guess) > 0:
			print ('How many times you have left ', num_guesses_allowed-counter)
			print ("This is so far what number you are guessing ", number_guess)
			#print("This is so far what number you are guessing ",' '.join(str_number_guess))
		input_number = int(input('put your number?' ))
		counter += 1
		number_guess.append(input_number)
		if input_number == magic_number:
			print ("You're got it right!")
			replay()
		elif input_number > magic_number:
			print ('You guessed too high')
		else:
			print ('You guessed too low')

	print ("Sorry you didn't guess in the", num_guesses_allowed,"times limit")
	replay()

def replay():
	play_state = input('do you want to play again y/n ')
	if play_state == "y":
		main()
	else:
		print ("Good bye!")
		exit()

# when user get it right, program should give options to play again or quick
# add while loop to increment i until 7 and break and if you get it correct then break too







if __name__ == '__main__':
    main()

