import random


computer_choice  = random.randint(1, 10)
chances = 5
print('please choose a number between 1 and 10')
user_choice = int(input())

while chances != 0:
    if (user_choice < 1 or user_choice > 10) and user_choice != None:
        print('Invalid number, please choose a number between 1 and 10')
        user_choice = int(input())
    else:
        if user_choice > computer_choice:
            print('Thats to high, please try again.')
            print('You have ',chances,' more chances. \n')
            user_choice = int(input())
            chances -= 1
        elif (user_choice < computer_choice):
            print('Thats to low, please try again.')
            print('You have ',chances,' more chances. \n')
            user_choice = int(input())
            chances -= 1
        else:
            print('Congrats you guessed right! The computer number is: ', computer_choice, '\n')
            break
