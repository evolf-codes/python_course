##### import python packages

import random as r
from random import choice as c

print(r.randint(1,5))


import keyword as k

def contains_keyword(*args):
    bools = [k.iskeyword(x) for x in args]
    if any(bools):
        return True
    else:
        return False

print(contains_keyword("shark",'a','False'))

print(k.iskeyword('return'))


##### import our own packages
import spotify_playlist
print(spotify_playlist.playlist)

#from Functions import exponent
#print(exponent(3,3))

import termcolor

print(termcolor.colored('Hello, World!', 'red'))