user_info={"name":"eric","date":"today","age":15}
print(user_info)
print(type(user_info))

#access variables from a dict
print(user_info['name'])

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = artist['first'] +" "+ artist['last']

# iterate over a dictionary - VALUES
for val in user_info.values():
    print(val)

# iterate over a dictionary - KEYS
for keys in user_info.keys():
    print(keys)

# iterate over a dictionary - KEYS and Values
for k,v in user_info.items():
    print(k,v)


donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

total_donations=0
for v in donations.values():
    total_donations = total_donations + v

print(total_donations)

# Dictionary Methods
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

# clear
#donations.clear()

# copy - will make a copy of the dictionary

donations_clone = donations.copy()
print(donations_clone)

#fromkeys - creates key value pairs from csv values

new_user = {}.fromkeys(['name','score','birthday'],'UNKOWN')
print(new_user)

# get
print(donations.get('sam'))


# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:

print(bakery_stock.get('o'))

if bakery_stock.get(food)!=None:
    print(str(bakery_stock.get(food)) + " left")
else:
    print("We don't make that")

# POP - remove a key value pair
bakery_stock.pop('morning bun')
print(bakery_stock)
# .popitem will remove item at random

# Update
bakery_stock.update({'morning bun':'2'})
print(bakery_stock)

# Dictionary Comprehension
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

squared_numbers = {k:v**2 for k,v in donations.items()}
print(squared_numbers)

# square the items in a list and store it in a dict
nums= {num: num**2 for num in [1,2,3,4]}
print(nums)

# interweave 2 lists
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i]:list2[i] for i in range(0,len(list1))}
print(answer)

# create a dictionary from lists
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# use the person variable in your answer
test = {k:v for k,v in person}
print(test)


# print dictionary of ascii characters
ascii = {x:chr(x) for x in range(65,91)}
print(ascii)