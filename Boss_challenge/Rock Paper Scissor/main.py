import random

decision = input("Enter Rock, Scissor or Paper: ").title()
choice= ["Rock", "Paper", "Scissor"]

randomm = random.choice(a)
print(f"Computer choose: {randomm}")

wins = {
    "Rock":"Scissor",
    "Paper":"Rock",
    "Scissor":"Paper"
}

if (decision == randomm):
    print("It's a tie, Play again")

elif decision not in choice:
    print("Invalid input!")

elif wins[decision] == randomm:
    print("You won!!")
else:
    print("You lost")
