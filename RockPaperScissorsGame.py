import random

choices = ["rock", "paper", "scissors"] 
#0 is tie
#1 is win
#-1 is lose
def normal_logic(user_choice=None):
    if user_choice is None:
        print("enter something")
        return
    choice = 3
    computer_choice = random.choice(choices)
    if computer_choice=="rock":
        choice = 0
    elif computer_choice=="paper":
        choice = 1
    else:
        choice = 2
    print(f"Computer chose: {computer_choice}, User chose: {user_choice}")
    
    if user_choice == computer_choice:
        return 0, choice
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return 1, choice
    else:
        return -1, choice

#any more specific logic goes here in a new method
