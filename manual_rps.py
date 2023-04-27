import random

def get_computer_choice():
    options = ["Rock", "Paper", "Scissors"]
    return random.choice(options)

def get_user_choice():
    return input("Enter your choice (Rock/Paper/Scissors): ")

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        return "It is a tie!"
    elif computer_choice == "Rock":
        if user_choice == "Paper":
            return "You won!"
        else:
            return "You lost!"
    elif computer_choice == "Paper":
        if user_choice == "Scissors":
            return "You won!"
        else:
            return "You lost!"
    elif computer_choice == "Scissors":
        if user_choice == "Rock":
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

