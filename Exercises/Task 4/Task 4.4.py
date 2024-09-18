import random
num=random.randrange(1,10)
guess= int(input('Guess a right number from 1 to 10:'))
while not guess ==num:
    print('The number is wrong!')
    if guess>num:
        print('Too high')
    elif guess<num:
        print('Too low')
    guess=int(input('Guess another number:'))
print('Correct')

