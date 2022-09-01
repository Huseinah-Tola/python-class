from bdb import Breakpoint
import random
def welcome():
	print('HI, Welcome to the Hangman game,Lets Begin')

	guess_category = input('''
	You are to choose from these categories:
	1. Fruits

	2. Food

	3. Drinks

	4. Desserts
	Now,
	Enter a number from 1 - 4:
	''')

	if guess_category.isalpha():
		print('You are to enter a number!')

	if guess_category.isspace():
		print('You have entered a space')

	if len(guess_category) > 1:
		print('only a number at a time')

	print('You have picked'+ ' ' + guess_category)
	return guess_category



def get_fruits():	
	fruits_list = ['orange','mango','avocado','apricot','pear']
	return random.choice(fruits_list)

def get_food():
	food_list = ['rice','beans','yam','pasta','potato']
	return random.choice(food_list)

def get_drinks():
	drinks_list = ['boba','coffee','milkshake','soda','cocktails']
	return random.choice(drinks_list)

def get_desserts():
	desserts_list = ['cake','yoghurt','ice cream','macarons','brownies','pudding']
	return random.choice(desserts_list)



def get_guess_category(number):
	guess_categories = {
    '1':get_fruits,
    '2':get_food,
    '3':get_drinks,
    '4':get_desserts
	}
	return guess_categories[number]
	

guess_word = get_guess_category(welcome())()


guess_name = ['*'] * (len(guess_word))


guess_lives = len(guess_word)
while guess_lives >= 0:

	guess_input = input('Guess a letter:')
	
	if len(guess_input) > 1:
		print('You have to input one letter at a time')

	if guess_input.isnumeric():
		print('You have to enter a letter')

	if guess_input.isspace():
		print('You have entered a space!')

	if(guess_input in guess_word):
		print('Correct!')
		letter_index = guess_word.index(guess_input)
		guess_name[letter_index] = guess_input	
		print(''.join(guess_name))

		if ''.join(guess_name) == guess_word:
			print('Yayyyy,You have guessed the word correct!')
			break
		

	elif guess_input.isalpha():
		print('You guessed wrong')
		guess_lives -=1
	
	

if guess_lives <= 0:
    print('You Have Used Up Your Lives')
good_bye_message = print('Thanks for Playing')