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