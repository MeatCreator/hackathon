import random

choices = ["rock", "paper", "scissors"]
choice = 4
#0 is tie
#1 is win
#-1 is lose
def normal_logic(user_choice=None):
    if user_choice is None:
        print("enter something")
        return
    
    computer_choice = random.choice(choices)
    choice= computer_choice
    print(f"Computer chose: {computer_choice}, User chose: {user_choice}")
    
    if user_choice == computer_choice:
        return 0
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return 1
    else:
        return -1

#any more specific logic goes here in a new method
