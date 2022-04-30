# __DUNDY__ -- do not touch
# CAPITAL_SNAKE_CASE -- should not be changed, global variable
# Snake_Case -- standard use

# common data types
#bool - T/F
#int - 1,2,3
#str- sequence of characters
#list - ordered sequence of values [1,2,3]
#dict - key value pair {k:val,k2:val2}

# variables can be dynamically changes - we can make an int into a string

# None is pythons version of null

name = None
name = "Eric"
name2 = 'Eric'
print(name, name2)

#escape characters
# \n new line
# \\ backslash

print("this is a backslash \n\\")

# concatendation
print(name + " " +name2)

# f strings - converts everything to a string
print(f"Your name is {name}")

first = "Eric"
last = "Volfson"

formatted = f"First Name: {first}, Last Name: {last}"
print(formatted)

# indexes
name="Luck"
print(name[0])

# converting data types
decimal = 1.23456
integer = int(decimal)
print (integer)


# comparison operators
# a==b checks if the VALUES are the same -- TRUE
# a is b checks if the VARIABLE are the same -- FALSE

a =[1]
b =[1]
print(a==b)
print(a is b)