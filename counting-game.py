import random

print int(random.uniform(1,10))

#game_level = int(raw_input("What's game level you want today? 1-easy, 2-medium, 3-challenge! "))

#print game_level

#print type(game_level)

def print_rule(game_level):
	print game_level
	if game_level == 1:
		print 'the magic game will radom pick the number from 1 to 100'
		print 'you have 7 times to guess what number it is!'
		print 'Good luck! start pick your number!'
	elif game_level == 2:
		print 'the magic game will radom pick the number from -100 to 100'
		print 'you have 7 times to guess what number it is!'
		print 'Good luck! start pick your number!'
	else:
		print 'the magic game will radom pick the number from -100 to 100'
		print 'you have 5 times to guess what number it is!'
		print 'Good luck! start pick your number!'




def main():
	game_level = int(raw_input("What's game level you want today? 1-easy, 2-soso, 3-hard! "))
	print game_level
	print type(game_level)
	print print_rule(game_level)

	

	while(True):
		import random
		magic_number = int(radom.uniform(1,100))
		input_number = int(raw_input('put your number? '))
		print type(magic_number)
		print type(input_number)
		if input_number == magic_number:
			if number > magic_number:
				print 'too high'
			else:
				print 'need more value'
		else:
			print "You're got it rigth!"

# add while loop to increment i until 7 and break and if you get it correct then break too







if __name__ == '__main__':
    main()

