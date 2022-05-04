
#for x in "hello"
for num in range(1,8):
    #print(num)
    print(num*num)

for letter in "coffee":
    print(letter*2)

# range(7) - 0-6 includes, does not include last number
# range(1,10,2) prints from 1,3,5,7,9
for num in range(1,10,2):
    print(num)


x = 0

# YOUR CODE GOES HERE:
for num in range(11,20,2):
    x = x +num
    print(x)
x = 0

# Repeater
print("How many times do I have to tell you?")
x = input()
x= int(x)

if isinstance(x, int):
    for num in range(0,x):
        print("CLEAN YOU ROOM")
else:
    print("ERROR")

# while
num =1
while num < 11:
    print(num)
    num = num +1