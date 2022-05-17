# OOP - use code to recreate things that exist in the world (objects, songs, calendar)
# CLASS - blueprints for objects (user class is a blueprint
# - every use has an email / password / login method)
# INSTANCE / OBJECT - a user object comes from the user class,
# it is made from the blueprint and contains everything defined in the class

# INHERITANCE - higher class takes all the functions of the lower class

# ENCAPSULATE - break up your code into smaller chunks- group PUBLIC and PRIVATE methods into a class
# PUBLIC things can be accessed outside, PRIVATE thigns accessed inside the class

# ABSTRACTION - expose only the RELEVANT data in a calss interpace, hiding private inner workings from users


class User:
    # STANDARD SPECIAL METHOD EVERY CLASS NEEDS
    # SELF keyword refers to the instance of the class
    # when referring to the INSANTE we use SELF
    # when referring to an input- we do not need to use SELF

    def __init__(self,first,last,age):
        self.first=first
        self.last=last
        self.age=age

    def full_name(self):
        return self.first, self.last

    def likes(self,thing):
        return f"{self.first} likes {thing}"

    def birthday(self):
        self.age = self.age +1
        return f"HAPPY BIRTHDAY, YOU ARE {self.age}!!!!!"

user1=User("eric",'red',32)
print(user1.first, user1.last)
print(user1.full_name())
print(user1.likes('CANDY'))
print(user1.birthday())

class Comment:
    def __init__(self,username,text,likes=0):
        self.username=username
        self.text=text
        self.likes=likes



c = Comment("eric","lol",3)
print(c.likes)

# _name --> convention - this is supposed to be a PRIVATE variable
# __name --> python will change the name of this attribute (name mangling, make this name particular to this CLASS, no conflicintg)
# __name__ --> these are specical / over write methos

#METHOD - is a function that is done on an OBJECT

class BankAccount():
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,num):
        self.balance = self.balance + num
        return self.balance

    def withdraw(self,num):
        self.balance = self.balance - num
        return self.balance

acct = BankAccount("Darcy")
print(acct.owner)
print(acct.balance)
print(acct.deposit(10))
print(acct.withdraw(3))
print(acct.balance)


# CLASS attributes are used to keep track of things WITHIN the class itself
# They are not on INSTANCE of the class

class Chicken():
    total_eggs = 0
    def __init__(self,species,name,eggs=0):
        self.species = species
        self.name = name
        self.eggs = eggs

    def lay_egg(self):
        self.eggs = self.eggs + 1
        Chicken.total_eggs = Chicken.total_eggs + 1
        return self.eggs

    def __repr__(self):  ### REPR is called when we print or call the class
        return self.name


c1=Chicken(name="eric",species="RED")
c2=Chicken(name="eric",species="BLUE")
print(Chicken.total_eggs)
c1.lay_egg()
c2.lay_egg()
print(Chicken.total_eggs)
print(c1)