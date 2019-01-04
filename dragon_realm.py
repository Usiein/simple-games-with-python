import time
import random

def displayIntro():
    print('''You are in a land full of dragons. In front of you \n
you see two caves. In one cave, the dragon is friendly \n
and will share his treasure with you. The other dragon \n
is greedy and hungry, and will eat you on sight. \n''')

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave... \n')
    time.sleep(2)
    print('It is dark and spooky... \n')
    time.sleep(2)
    print('A large dragon jumps in front of you! He opens his jaws and... \n')
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Shares his treasure with you! \n')
    else:
        print('Gobbles you down in one bite! \n')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    displayIntro()

    caveNumber = chooseCave()

    checkCave(caveNumber)

    playAgain = input('Do you want to play again? (yes/no) \n')
