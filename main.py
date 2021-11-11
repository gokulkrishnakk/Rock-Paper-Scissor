from time import sleep
import start

name = None


def data():
    globals()['name'] = input('Hi user, whats your name? ').upper()
    sleep(1)
    print('Hi', name, 'welcome to the game rock-paper-scissor')
    sleep(2)
    print('There wll be 3 rounds in the game')
    sleep(2)
    print('You can choose rock, paper or scissor as your weapon')


data()

choices_available = ['rock', 'paper', 'scissor']
user = None

start.game()


def result():
    print('\n \n \n', name, ':', start.user_point)
    print('COMPUTER:', start.computer_point)
    sleep(2)
    if start.user_point > start.computer_point:
        print('You win!')
    if start.user_point == start.computer_point:
        print('Tie!')
    if start.computer_point > start.user_point:
        print('Computer won!')


result()
print('Bye')
