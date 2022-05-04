import random


guess = None
num = random.randint(1, 10)

while True:

    print("Guess a number between 1 and 10: ")
    guess = int(input())

    if guess > num:
        print("Too high try again")
    if guess < num:
        print("Too low try again")
    if guess == num:
        print("You GOT IT!!!!!!!\nDo you want to play again (y/n)")
        ans = input()
        if ans == 'n':
            break
        else:
            num = random.randint(1, 10)



