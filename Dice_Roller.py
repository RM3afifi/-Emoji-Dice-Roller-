#!/usr/bin/python3.9

# Filename: Dice_Roller.py
  
# Importing randome module
import random
print("😋🎲Emoji Dice Roller🎲😋")
# The name of the app
print(" Made by Rokaya Muhammad")
# The name of who made the app(Me)
print("Hi, What's your name?📝")
# Ask about the user's name
Name = input("Name: ")
print("Hello",Name,"!👋")
# Welcoming the user

# Initiating an while loop to keep the program executing
while True:
    print("Rolling Dice...🎲")	
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    # Using random.randint(1,6) to generate a random value between 1 & 6
    print(f"It\'s", random.randint(1,6), "😘😍")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")    

    # Asking user to roll the dice again or quit 
    repeat = input("Roll Dice again? 'y' for yes & 'n' for no: ")

    if repeat == 'n':
        print("Bye",Name,"!👋")
        # Saying bye to the user
        print("Enjoy your time!")
        break
