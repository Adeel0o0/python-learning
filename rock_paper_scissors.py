import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper or scissors: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game ended")
        exit = True
    
    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock")
            print("computers input is rock")
            print ("It is a tie!")
    elif computer_input == "paper":
            print("Your input is rock")
            print("computers input is paper")
            print ("computer wins")
            computer_points += 1
    elif computer_input == "scissors":
            print("Your input is rock")
            print("computers input is scissors")
            print ("You win")
            user_points += 1

    elif user_input == "paper":
        if computer_input == "rock":
            print("Your input is paper")
            print("computersinput is rock")
            print ("You win")
            user_points += 1
    elif computer_input == "paper":
            print("Your input is paper")
            print("computers input is paper")
            print ("It is a tie!")
    elif computer_input == "scissors":
            print("Your input is paper")
            print("computers input is scissors")
            print ("computer wins")
            computer_points += 1

    elif user_input == "scissors":
        if computer_input == "rock":
            print("Your input is scissors")
            print("computers input is rock")
            print ("computer wins")
            computer_points += 1
    elif computer_input == "paper":
            print("Your input is scissors")
            print("computers input is paper")
            print ("You win")
            user_points += 1
    elif computer_input == "scissors":
            print("Your input is scissors")
            print("computers input is scissors")
            print ("It is a tie!")
    
    elif user_input != "rock" or user_input != "paper" or user_input != "scissors":
        print("Invalid input")






