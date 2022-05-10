def square(num):
    return num * num

# lambdas are single line functions - anonymous / portable functions
square2 = lambda num: num * num

print(square(7))
print(square2(7))

# map - takes 2 arguments 1) iterable 2) function -- it will run the function for each
# element of the iterable

nums = [1,2,3,4]

doubles = map(lambda x : x*2, nums)
print(doubles)
print(list(doubles))

def decrement_list(lst):
    return list(map(lambda n: n-1,lst))

print(decrement_list([1,2,3]))


# filter - takes 2 arguments 1) iterable 2) function -- it will run the boolean True or Falce
# if it meets the filter condition

users = [
    {"username":"sam", "tweets":["hello","goodbye"]},
    {"username":"dee", "tweets":[]},
    {"username":"bee", "tweets":[]},
]

# filter out all inactive users


inactive = filter(lambda n: len(n['tweets'])==0, users)
inactive = list(inactive)
print(inactive)
print([x.get('username') for x in inactive])


# oneline solution
usernames = list(map(lambda u: u['username'],
    filter(lambda n: len(n['tweets'])==0,users)))

print(usernames)

# list comprehension way to do it
print([x.get('username') for x in users if len(x.get('tweets'))==0])



def remove_negatives(lst):
    return list(filter(lambda n: n>=0, lst))


# ANY and ALL
# All - accepts an iterable argument and returns BOOL TRUE, only if ALL are TRUE
# ANY - accepts an iterable argument and returns BOOL TRUE, only if ANY are TRUE
# return TRUE if it contains ONLY string


print(type('s'))
def is_all_strings(lst):
    return all([isinstance(x, str) for x in lst])

print(is_all_strings(['1','2','3']))


# SORTED
# works with iterable collections other than lists, tuples as well
# it does not change the variable

nums=[1,2,4,2,1,100,5,100,5]
print(sorted(nums))

users = [
    {"username":"sam", "tweets":100},
    {"username":"dee", "tweets":8},
    {"username":"bee", "tweets":100000},
]

print(sorted(users,key=lambda u:u['tweets']))


### MAX / MIN
# takes in an interable and a function -- performs the function and returns an instance of the iterable
nums=[1,2,4,2,1,10000,5,100,5]
print(max(nums))

names = ['arya','kermit','simpsonssssonnn']
# print the longest name

print(max(names, key=lambda n:len(n)))

# print users with least tweets

users = [
    {"username":"sam", "tweets":100},
    {"username":"dee", "tweets":8},
    {"username":"bee", "tweets":100000},
]

print(min(users,key= lambda u:u['tweets'])['username'])

# get the min and max for any elements

def extremes(lst):
    mn=min(lst)
    mx=max(lst)
    return(mn,mx)

print(extremes([1,2,3,4,5]))

# ABSOLUTE Values abs()
# SUM - adds all the elements in the iterable - left to right

print(abs(-100))
print(sum([1,2,3]))
print(round(1.1234567,3))

'''
sum_even_values(1,2,3,4,5,6) # 12
sum_even_values(4,2,1,10) # 16
sum_even_values(1) # 0
'''

# define sum_even_values

def sum_even_values(*args):
    evens = [x for x in args if x%2==0]
    return sum(evens)
print(sum_even_values(1,2,3,4,5,6))


# define sume of floats

'''
sum_floats(1.5, 2.4, 'awesome', [], 1) # 3.9
sum_floats(1,2,3,4,5) # 0
'''

def sum_floats(*args):
    floats = [x for x in args if (isinstance(x, float))]
    if floats:
        return sum(floats)
    else:
        return 0

print(sum_floats(1.5, 2.4, 'awesome', [], 1))


# ZIP funcitons - put together 2 lists and pair them in tuples

nums1=[1,2,3,4,5]
nums2=[0,0,0,0,0,0,0,0]

z=zip(nums1,nums2)
print(dict(z))


def interleave(s1,s2):
    lst = list(zip(s1,s2))
    lst2 = [''.join(x) for x in lst]
    result =''
    for x in lst2:
        result = result + ''.join(x)
    return result

print(interleave('hie','hae'))


# filter out every number not divisible by 4, and triple every remaining number
'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''

def triple_and_filter(lst):
    #return [x*3 for x in lst if x%4==0]
    fil = list(filter(lambda x: x%4==0,lst))
    triple= map(lambda x: x*3, fil)
    return list(triple)
print(triple_and_filter([1,2,3,4]))

'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]


print(list(map(lambda x: x.get('first')+" "+ x.get('last'), names)))

#def extract_full_name(lst):

