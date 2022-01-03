import random

random_number = random.randint(0, 2)
computer_move = "rock"

if random_number == 0:
    computer_move = "rock"
elif random_number == 1:
    computer_move = "paper"
elif random_number == 2:
    computer_move = "scissor"

player_1 = input("start the player_1:").lower()
player_2 = computer_move


if player_1 == player_2:
    print("You became equal...")
elif player_1 == "rock":
    if player_2 == "scissor":
        print("You won the player_1")
    elif player_2 == "paper":
        print("You won the player_2")
elif player_1 == "paper":
    if player_2 == "rock":
        print("You won the player_1")
    elif player_2 == "scissor":
        print("You won the player_2")
elif player_1 == "scissor":
    if player_2 == "paper":
        print("You won the player_1")
    elif player_2 == "rock":
        print("You won the player_2")
else:
    print("something went wrong...")
