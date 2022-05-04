import random

mylist = ["rock", "paper", "scissors"]

print("...rock...\n...paper...\n...scissors...\n")

# player_1_choice = random.choice(mylist)
# player_2_choice = random.choice(mylist)

# print(player_1_choice)
# print(player_2_choice)


ans = True
while ans:

    p1_win = 0
    p2_win = 0
    print(ans)

    while (p1_win < 2) and (p2_win < 2):
        player_1_choice = random.choice(mylist)
        player_2_choice = random.choice(mylist)

        if player_1_choice == player_2_choice:
            print("DRAW")
        elif player_1_choice == "rock" and player_2_choice == "scissors":
            print("PLAYER 1 WINS")
            p1_win = p1_win + 1
        elif player_1_choice == "scissors" and player_2_choice == "paper":
            print("PLAYER 1 WINS")
            p1_win = p1_win + 1
        elif player_1_choice == "paper" and player_2_choice == "rock":
            print("PLAYER 1 WINS")
            p1_win = p1_win + 1
        else:
            print("PLAYER 2 WINS")
            p2_win = p2_win + 1

    print(f"player 1 wins:{p1_win} \nplayer 2 wins:{p2_win} \nplay again (1/0)")
    ans = input()
    ans = int(ans)
    print(ans)
    if ans == False:
        break
    else:
        continue
