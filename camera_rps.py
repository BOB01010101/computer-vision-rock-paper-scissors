import random

import numpy as np

import keras_model as km 

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

def get_prediction(model):
    
    predicted_class = np.argmax(model[0])

    class_names = ["nothing", "rock", "paper", "scissors"]
    predicted_class_name = class_names[predicted_class]

    return predicted_class_name

def play_1():
    computer_choice = get_computer_choice()
    user_choice = get_prediction(km.run(["python", "keras_model.h5"])  )
    print(get_winner(computer_choice, user_choice))

play_1()

#This code creates a new function called get_prediction 
#It then returns the predicted class name with the highest probability.

#The play_1 function calls get_prediction instead of get_user_choice to get the user’s choice
# When run, this code will play a game of Rock-Paper-Scissors using the 
#output of the computer vision model.

def play_2():
    computer_choice = get_computer_choice()
    
    print("Rock...")
    time.sleep(1)
    
    print("Paper...")
    time.sleep(1)
    
    print("Scissors...")
    time.sleep(1)
    
    user_choice = get_prediction(km.run(["python", "keras_model.h5"]))
    
    print(f"You chose {user_choice}")
    
    print(get_winner(computer_choice, user_choice))

play_2()

#This code adds a countdown before getting the user’s choice
#It uses the time.sleep function to pause for one second between each countdown message.


