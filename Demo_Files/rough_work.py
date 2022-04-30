from random import choice

food = choice(['apple', 'grape', 'bacon', 'steak', 'worm', 'dirt'])
# NO TOUCHING =============================================


# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
print(food)
if food == 'apple' or food == 'grape':
    print('fruit')
elif food == 'bacon' or food == 'steak':
    print('meat')
else:
    print('yuck')

#########


# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| \
from random import randint                           #|  \
x = randint(-100, 100)                               #|   \
while x == 0:  # make sure x isn't zero              #|    \
    x = randint(-100, 100)                           #|     NO TOUCHING!!!!!! (please)
y = randint(-100, 100)                               #|    /
while y == 0:  # make sure y isn't zero              #|   /
    y = randint(-100, 100)                           #|  /
# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| /



# Don't change the print statements so the tests can pass!
# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

if (x>0) and (y>0):
    print("both positive")
elif (x<0) and (y<0):
    print("both negative")
elif (x>0) and (y<0):
    print("x is positive and y is negative")
elif (y>0) and (x<0):
    print("y is positive and x is negative")
else:
    print('error')
# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


######


# NO TOUCHING ======================================

from random import choice, randint

# randomly assigns values to these four variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

# NO TOUCHING ======================================

calling_in_sick = None

if actually_sick and sick_days >0:
    calling_in_sick = True
elif (kinda_sick and hate_your_job) and sick_days >0:
    calling_in_sick = True
else:
    calling_in_sick = False

print(calling_in_sick)
  # set this to True or False with Boolean Logic and Conditionals!
