import random

print('Hello, what is your name?')
name = input()
print('Well, ' + name + ', I\'m thinking of a number between 1 and 100000.')
number = random.randint(1, 100000)
guessesTaken = 0

while guessesTaken < 20:
    print('Take a guess.')
    guess = int(input())
    guessesTaken += 1
    if guess == number:
        print('You\'re right!')
        break
    elif guess >= number:
        print('Too big.')
        continue
    elif guess <= number:
        print('Too small.')
        continue

if guess == number:
    print('Congrats, ' + name + ', you`ve guessed right number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope, the number I was thinking of is ' + str(number))
