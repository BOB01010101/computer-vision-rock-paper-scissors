import random

def get_computer_choice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def get_user_choice():
    return input("Enter your choice (rock/paper/scissors): ")

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        return "It is a tie!"
    elif computer_choice == "rock":
        if user_choice == "paper":
            return "You won!"
        else:
            return "You lost!"
    elif computer_choice == "paper":
        if user_choice == "scissors":
            return "You won!"
        else:
            return "You lost!"
    elif computer_choice == "scissors":
        if user_choice == "rock":
            return "You won!"
        else:
            return "You lost!"

computer_choice = get_computer_choice()
user_choice = get_user_choice()

print(get_winner(computer_choice, user_choice))

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    print(get_winner(computer_choice, user_choice))

play()

