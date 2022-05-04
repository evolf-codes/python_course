for num in range(1,21):
    if num == 4 or num ==13:
        print(f"{num} is unlucky")
    elif num%2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")



## copying me loop

# key = "stop copying me"
#
# print("Hey how's it going?")
# ans = input()
#
# while ans != key:
#     print(ans)
#     ans = input()
# print("YOU WIN")

from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 # store random number in here, each time through
i = 0  # i should be incremented by one each iteration

while number != 5:
    number = randint(1,10)
    i = i+1
    print(number)


