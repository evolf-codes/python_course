import termcolor
from pyfiglet import Figlet

colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

while True:
    print(f"Please pick a colour from the following: {colors}")
    user_color = input()

    if user_color in colors:
        user_color = user_color.lower()
        break
    else:
        print("Please pick another colour")

while True:
    print(f"Please pick a message to write")
    user_msg = input()

    if user_msg:
        break
    else:
        print("Please pick another msg")

f = Figlet(font='5lineoblique')
x = f.renderText(user_msg)

print(termcolor.colored(x, user_color))
