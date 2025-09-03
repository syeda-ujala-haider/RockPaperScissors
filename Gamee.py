import random

def check_win(player, computer):
    if player == computer:
        return "It's a DRAW!"
    elif (player == "r" and computer == "s") or (player == "p" and computer == "r") or (player == "s" and computer == "p"):
        return "YOU WIN!"
    else:
        return "YOU LOSE!"

print("Welcome to Rock-Paper-Scissors Game!".center(60), "\n")

choices = ["r", "p", "s"]

while True:
    
    player = input("Enter r for Rock, p for Paper, s for Scissors, or q to Quit: ").lower()

    
    if player == "q":
        print("\nThanks for playing! Goodbye 👋")
        break

    
    if player not in choices:
        print("Invalid choice! Please try again.\n")
        continue

    
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    
    result = check_win(player, computer)
    print(result, "\n")
