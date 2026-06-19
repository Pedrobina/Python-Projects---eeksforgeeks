import random

words = ['pikachu', 'buterfree', 'psyduck', 'togepi', 'blastoise', 'venussaur', 'bubassaur', 'charmander', 'squirtle','onix', 'geodude', 'zubat','totodille', 'vulpix', 'Mr. Mine', 'meowth', 'arbok','weezing']
word = random.choice(words)
guesses = []
turns = 12

print('Please guess the Pokemon:\n')
while turns > 0:
    print('Letters founded so far:')
    print(guesses)
    print('Tentatives ', turns)
    print('Please enter a letter:')
    letter = str(input())
    for l in word:
        if l == letter:
            guesses.append(l)
    turns-=1

