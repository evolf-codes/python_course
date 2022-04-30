import random
mylist=["rock","paper","scissors"]


print("...rock...\n...paper...\n...scissors...\n")

player_1_choice = random.choice(mylist)
player_2_choice = random.choice(mylist)

print(player_1_choice)
print(player_2_choice)


if player_1_choice == player_2_choice:
    print("DRAW")
elif player_1_choice == "rock" and player_2_choice == "scissors":
    print("PLAYER 1 WINS")
elif player_1_choice == "scissors" and player_2_choice == "paper":
    print("PLAYER 1 WINS")
elif player_1_choice == "paper" and player_2_choice == "rock":
    print("PLAYER 1 WINS")
else:
    print("PLAYER 2 WINS")