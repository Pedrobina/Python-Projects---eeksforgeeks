import random

user_choice = 0
computer_choice  = random.randint(1, 10)
chances = 5

while chances != 0:
    if user_choice != computer_choice:
        print('Please choose a number between 1 and 10')
        print('You have ',chances,' more chances.')
        user_choice = int(input())
        chances -= 1
    else:
        print('Congrats you guessed rigth! The computer number is: ', computer_choice)
        break
