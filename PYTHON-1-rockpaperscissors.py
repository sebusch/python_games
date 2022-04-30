#!/usr/bin/env python3

import random 

answer_dict = {1: "Rock", 2: "Paper", 3: "Scissors"}
computer_play = random.randint(1,3)

print("\nWelcome to Rock, Paper, Scissors!\n")

print_str = "Enter:"
for key, value in answer_dict.items():
    print_str += f"\n{key} for {value}"
    
print(print_str)

user_play = int(input("Enter your number to play:  "))

if user_play not in answer_dict.keys():
    print("You did not enter a valid number")


print(f"\nYou chose: {answer_dict[user_play]}")
print(f"Computer chose: {answer_dict[computer_play]}\n")

# Find conditions where user wins:
# this is when user:computer = 2:1, 3:2, 1:3
if user_play == computer_play:
    print("We have a tie!")
elif (user_play - computer_play == 1) or (computer_play - user_play == 2):
    print("User wins!!!")
else:
    print("Sorry, computer wins :(")
