# rock paper scissors >:)
import random

choice_pool = ["rock", "paper", "scissors"]

def rpc_input():
    user_input = input("rock paper scissors! (type 'exit' to exit) pick one: \n").lower()
    computer_input = random.choice(choice_pool)
    if user_input not in (choice_pool):
        print("not a valid input!")
        exit()
    if user_input == computer_input: 
        print(f"tie! computer chose {computer_input} and you chose {user_input}!")
        exit()
    if user_input == "exit":
        exit()
    if user_input == "rock" and computer_input == "paper":
        print(f"computer's {computer_input} beats {user_input}! try again!")
    elif user_input == "paper" and computer_input == "scissors":
        print(f"computer's {computer_input} beats {user_input}! try again!")
    elif user_input == "scissors" and computer_input == "rock":
        print(f"computer's {computer_input} beats {user_input}! try again!")
    else:
        print(f"you win! :D {user_input} beats computer's {computer_input}")

while True:
    rpc_input()