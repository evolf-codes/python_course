
lst = []
print(len(lst))

## ADD #################
#Insert
lst.insert(1,'cat')

# APPEND
lst.append('a')
print(lst)

# EXTEND
lst.extend(['b','c'])
print(lst)


# DELETE ###################

#Clear - remove everyting
#lst.clear()

#POP - remove at an index (can be stored in a variable)
itm = lst.pop(2)
print(itm)

#Remove - remove the first item which value matches x, otherwise error
lst.remove('a')
print(lst)


# Index - return the position where that value exists
lst=[1,1,2,3,4,5,6]
print(lst.index(1))
# Count - returns the number or times a value exists

lst=[1,1,2,3,4,5,10,6]
print(lst.count(1))

# sort
lst.sort()
print(lst)

# reverse
lst.reverse()
print(lst)

# Join
words = ['hello', 'i', 'am', 'eric']
concat = " ".join(words)
print(concat)



# SLICE
print(lst[0:2])

# reverse a string
stg = "this is fun"
print(stg[::-1])

# modify portion of list
num = [1,2,3,4,5,6]
num[0:2] = [10,20,30]
print(num)

# swapping values
names = ['e','v']
names[0],names[1]=names[1],names[0]
print(names)


# List comprehension
num = [1,2,3,4,5,6]
new_num = [x*10 for x in num] #multiply each by 10
print(new_num)

name = 'eric'
new_name=[char.upper() for char in name]
print(new_name)

# List comprehension with conditional logic
# get all even numbers
num = [1,2,3,4,5,6]
evens = [x for x in num if x%2 == 0]
print(evens)

# multipy even by 2, divide odd by 2
cond = [x*2 if x%2 == 0 else x/2 for x in num]
print(cond)

# first character of each word
names = ['Elise','Tim','Matt']
answer = [x[0] for x in names]
print(answer)

# print only divisible by 12
answer =  [x for x in range(1,101) if x%12==0]
print(answer)

# print without values
val = 'amazing'
answer = [x for x in val if x not in list('aeiou')]
print(answer)

# nested lists
answer = [[i for i in range(3)]for x in range(3)]
print(answer)

# create nested list without list comprehension
lst=[]
lst2=[]
for x in range(10):
    lst.append(x)
    for num in range(10):
        lst2.append(lst)
print(lst2)