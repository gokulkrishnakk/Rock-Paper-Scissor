from time import sleep
from random import *

choices_available = ['rock', 'paper', 'scissor']
user = None

user_point = 0
computer_point = 0


def game():
    for i in range(3):
        sleep(2)
        print('\n\n')

        globals()['user'] = input('Take your weapon:').lower()

        computer = choice(choices_available)
        print('COMPUTER:', computer)
        sleep(2)

        if computer == user:
            print('Tie')
            globals()['computer_point'] += 5
            globals()['user_point'] += 5
        else:
            if user == 'rock' and computer == 'paper':
                print('You loose')
                globals()['computer_point'] += 10
            if user == 'rock' and computer == 'scissor':
                print('You win')
                globals()['user_point'] += 10
            if user == 'paper' and computer == 'rock':
                print('you win')
                globals()['user_point'] += 10
            if user == 'paper' and computer == 'scissor':
                print('You loose')
                globals()['computer_point'] += 10
            if user == 'scissor' and computer == 'rock':
                print('You loose')
                globals()['computer_point'] += 10
            if user == 'scissor' and computer == 'paper':
                print('you win\n \n \n')
                globals()['user_point'] += 10
