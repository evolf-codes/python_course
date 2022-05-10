import numpy

### RETURN will EXIT the FUNCTION~!!!!!!
####
###

def square_num(x):
    return x*x

result = square_num(7)
print(result)

import random
def coin_flip():
    x=['heads','tails']
    return random.choice(x)

print(coin_flip())

def generate_evens():
    return ([x for x in range(1,50) if x%2==0])

def exponent(num,power=2):
    return  num ** power

print(exponent(5))

def add(a,b):
    return a+b

def subrtact(a,b):
    return a-b

def maths(a,b,fn=add):
    return fn(a,b)

print(maths(2,5))
print(maths(2,5,subrtact))

### SCOPE - inside fucntions we can only manipulate local variables,
# otherwise we need the keyword global


## days

def return_day(num):
    day = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    mapping = {x:day[x] for x in range(0,7)}
    print(mapping)
    if int(num)-1 <=7:
        return mapping.get(num-1)
    else:
        return None

print(return_day(10))

# last element

element_list =[1,2,3]
def last_element(element_list):
    if element_list:
        return element_list[-1]
    else:
        return "this list is empty"

print(last_element(element_list))


# letter count
'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

#define single_letter_count below:

def single_letter_count(str,ltr):
    return str.upper().count(ltr.upper())

print(single_letter_count("Hello World", "z") )


'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

# flesh out multiple_letter count:
def multiple_letter_count(x):
    return {ltr.lower():x.count(ltr.lower()) for ltr in x.lower()}

print(multiple_letter_count("hhhhiiiii"))

'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(lst,cmd,place,val=None):
    if cmd =="remove" and place == 'end':
        return lst.pop()
    if cmd =="remove" and place == 'beginning':
        return lst.pop(0)
    if cmd =="add" and place == 'end':
        lst.append(val)
        return lst
    if cmd =="add" and place == 'beginning':
        lst.insert(0,val)
        return lst
    else:
        return "error - missing values"

print(list_manipulation([1,2,3], "remove", "end"))
print(list_manipulation([1,2,3], "remove", "beginning") )
print(list_manipulation([1,2,3], "add", "beginning", 20))
print(list_manipulation([1,2,3], "add", "end", 30))

'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

word = "hello"
print(word[::-1])
def is_palindrome(word):
    word = word.lower()
    if word == word[::-1]:
        return True
    else:
        return False
print(is_palindrome('amanaplanacanalpanama'))

'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''


def frequency(lst, term):
    return lst.count(term)

print(frequency([1,2,3,4,4,4], 4))


'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers(lst):
    even_list = [x for x in lst if x%2==0]
    #return numpy.prod(even_list)
    result = 1
    for x in even_list:
        result = result * x
    return result

print(multiply_even_numbers([2,3,4,5,6]))

'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''

def capitalize(str):
    return str[0].upper()+str[1:]

print(capitalize("tim"))

'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''

def compact(lst):
    return [x for x in lst if bool(x)==True]

print(compact([0,1,2,"",[], False, {}, None, "All done"]) )

'''intersection values'''

lst1=[1,2,3,4,5]
lst2=[4,5,6,3]

def intersection(lst1,lst2):
    return [x for x in lst1 if x in lst2]

print(intersection(lst1,lst2))

'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''

def partition(lst,isEven):
    truthy_list=[]
    falsy_list=[]
    for x in lst:
        if isEven(x):
            truthy_list.append(x)
        else:
            falsy_list.append(x)
    return [truthy_list,falsy_list]

def isEven(num):
    return num % 2 == 0

print(partition([1,2,3,4], isEven))


### * ARGS
# when you have to pass in an unknown amount of perameters
# it takes in everything you pass in as a tuple

def sum_all_nums(*args):
    total =0
    for num in args:
        total = total + num
    return total

print(sum_all_nums(1,2,3,4,5,6))


def contains_purple(*args):
    if ("purple" in args):
        return True
    else:
        return False

print(contains_purple("purple",2))

### ** KWARGS - stores the arguments in a dictionary

def fav_colours(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}'s fav color is {v}!")
fav_colours(eric='red',sam='blue')

def combine_words(wrd,**kwargs):
    if 'prefix' in kwargs.keys():
        return (kwargs['prefix'])+wrd
    if 'suffix' in kwargs.keys():
        return wrd+(kwargs['suffix'])
    else:
        return wrd

print(combine_words("child",suffix="in"))


### unpacking

## unpack list/ tuple *
## unpack dictionary **

# NO TOUCHING! =================================================================
def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
# NO TOUCHING! =================================================================

# Write your code below:

result1 = count_sevens(1,4,7)

result2 = count_sevens(*nums)



'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''

def calculate(message="The result is",**args):
    if args['operation'] =='add':
        result = args['first']+args['second']
    if args['operation'] =='subtract':
        result = args['first'] + args['second']
    if args['operation'] =='multiply':
        result = args['first'] * args['second']
    if args['operation'] =='divide':
        result = args['first'] / args['second']
    if args['make_float']==False:
        result = int(result)
    else:
        result = float(result)
    return message+ " " + str(result)

print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
print(calculate(make_float=True, operation='divide', first=3.5, second=5))
