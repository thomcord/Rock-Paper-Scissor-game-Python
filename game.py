from random import randint

choice = ["rock", "paper", "scissors"]

computer = choice[randint(0,2)]

print("This is the Rock, Paper and Scissors Game!\n")
player = input("Your Choice: ").lower()
print("Computer choice: " + computer)

if player == computer:
    print("Draw")
elif player == "rock" and computer == "paper":
    print("Computer wins.")
elif player == "rock" and computer == "scissors":
    print("Player wins.")
elif player == "paper" and computer == "rock":
    print("Player wins.")
elif player == "paper" and computer == "scissors":
    print("Computer wins.")
elif player == "scissors" and computer == "rock":
    print("Player wins.")
elif player == "scissors" and computer == "paper":
    print("Computer wins.")
    
print("End of the game.")
print("--------------------")

