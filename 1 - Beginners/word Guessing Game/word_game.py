import random

pokemons = ['pikachu', 'buterfree', 'psyduck', 'togepi', 'blastoise', 'venussaur', 'bubassaur',
          'charmander', 'squirtle','onix', 'geodude', 'zubat','totodille', 'vulpix', 'voltorb', 'meowth', 'arbok','weezing']
pokemon = random.choice(pokemons)
guesses = []
turns = 12

#Create the blank size of the name of the pokemon
for p in pokemon:
    guesses.append('_')

print('Please guess the Pokemon:\n')
while turns > 0:
    print('Letters founded so far:')
    print(guesses)
    print('Tentatives ', turns)
    print('Please enter a letter:')
    letter = str(input())
    
    # validate the name by searching the letter in the vettor
    for x in pokemon:
        if x == letter:
            i = pokemon.index(x)
            guesses[i] = letter  

    if guesses.index('_') < 0:
        print('Your Pokemon was founded')
    turns-=1

