
player_1 = input("start the player_1:")
player_2 = input("start the player_2:")

if player_1 == "rock" and player_2 == "scissor":
    print("You won the player_1")
elif player_1 == "rock" and player_2 == "paper":
    print("You won the player_2")
elif player_1 == "paper" and player_2 == "rock":
    print("You won the player_1")
elif player_1 == "paper" and player_2 == "scissor":
    print("You won the player_2")
elif player_1 == "scissor" and player_2 == "paper":
    print("You won the player_1")
elif player_1 == "scissor" and player_2 == "rock":
    print("You won the player_2")
elif player_1 == player_2:
    print("You became equal...  :)")
