# ask for age
# 18 - 21 wristband
# 21+ normal entry
# too young, sorry

print("please enter your age")
age=input()
if age:
    age = int(age)
    if (age >=18 and age<=21):
        print("WRISTBAND")
    elif age > 21:
        print("21+ normal entry")
    else:
        print("too young, sorry")
else:
    print("error")



