import tkinter as tk
import random

# Define choices and mapping to images
choices = ["rock", "paper", "scissors"]

# Function to determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Function to handle player's choice
def play(choice):
    computer_choice = random.choice(choices)
    player_choice_label.config(text=f"Player's Choice: {choice}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"Result: {result}")

# Create the main window
window = tk.Tk()
window.title("Neha's RPS Game")

# Add a title label
title_label = tk.Label(window, text="Lets play Rock, Paper, Scissors", font=("Helvetica", 16))
title_label.pack(pady=10)

# Create frame for choice buttons
frame = tk.Frame(window)
frame.pack(pady=10)

# Add buttons for Rock, Paper, Scissors
rock_button = tk.Button(frame, text="Rock", width=15, command=lambda: play("rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(frame, text="Paper", width=15, command=lambda: play("paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(frame, text="Scissors", width=15, command=lambda: play("scissors"))
scissors_button.grid(row=0, column=2, padx=5)

# Add labels to display choices and result
player_choice_label = tk.Label(window, text="Player's Choice: ", font=("Helvetica", 12))
player_choice_label.pack(pady=5)

computer_choice_label = tk.Label(window, text="Computer's Choice: ", font=("Helvetica", 12))
computer_choice_label.pack(pady=5)

result_label = tk.Label(window, text="Result: ", font=("Helvetica", 12))
result_label.pack(pady=10)

# Start the main event loop
window.mainloop()
