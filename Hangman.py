print('Welcome to the Hangman game, Lets begin')

guess_keyword = 'FRUIT'

guess_hint = 'Looks like an Orange but has an hard core on the inside' #guess_word hint
print('Here is an hint for you;',guess_hint)

guess_word = 'mango'

guess_name = ['*','*','*','*','*'] 
print(guess_name) 

guess_lives = len(set(guess_word))
while guess_lives >= 0:
    guess_input = input('Guess a letter:')

    if len(guess_input) > 1:
        print('You have to input one letter at a time')

    if guess_input.isnumeric():
        print('You have to enter a letter')

    if guess_input.isspace():
        print('You have entered a space!')
        

    # for item in guess_word:
    if(guess_input  in guess_word):
        print('correct')
        letter_index = guess_word.index(guess_input)
        guess_name[letter_index] = guess_input
        print(''.join(guess_name))

        if ''.join(guess_name) == guess_word:
            print('You have guessed the fruit right!')
            break
    elif guess_input.isalpha():
        print('You guessed wrong')
        guess_lives -= 1
    

if guess_lives <= 0:
    print('You Have Used Up Your Lives')

print(guess_word,',''Thanks for Playing!')