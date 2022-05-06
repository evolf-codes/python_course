# tuple - immutible - cannot be changed , makes you code SAFER and FASTER
months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
for i in months:
    print(i)

# count how many times and item in tuples
# index will tell us where it exists

# tuples can be used as keys in a dictionary
locations = {
    (5.12, 5.243): "Tokyo",
    (5.12, 5.245):"Paris"
}

print(locations.items())

# Sets - cannot have duplicate values ,
# there is no order
# you cannot access item by index because there is no order

set = {1,2,2,3,4,5}
print(set)

# adding values
set.add(6)
print(set)

# remove values
set.remove(6)
print(set)

# set comprehension
print({x**2 for x in range(10)})

print({char.upper() for char in 'hellooooo'})

def are_all_vowels_in_string(string):
    return len({char for char in string if char in 'aeiou'}) == 5

print(are_all_vowels_in_string("ericisthebest"))