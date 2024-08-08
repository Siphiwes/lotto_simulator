import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# Parameters
total_numbers = 49
pick_numbers = 5
drawn_numbers = 7

# Function to generate a random set of numbers
def generate_numbers(n, k):
    return set(random.sample(range(1, n+1), k))

# Function to simulate the lotto drawing and check the player's numbers
def simulate_lotto(player_numbers):
    # Lottery machine draws 7 numbers
    machine_numbers = generate_numbers(total_numbers, drawn_numbers)
    
    # Check how many numbers the player got right
    correct_numbers = len(player_numbers & machine_numbers)
    
    return machine_numbers, correct_numbers

# Function to handle the play button click
def on_play():
    try:
        # Get number of bets from the user
        num_bets = simpledialog.askinteger("Number of Bets", "How many sets of numbers do you want to bet on?")
        if num_bets is None or num_bets < 1:
            return
        
        results = []
        for i in range(num_bets):
            # Ensure we have enough entry fields
            if i >= len(entries):
                raise ValueError("Not enough bets configured.")
            
            # Get player numbers from the entry fields
            player_numbers = {int(entry.get()) for entry in entries[i]}
            if len(player_numbers) != pick_numbers:
                raise ValueError("Please pick exactly 5 unique numbers.")

            if any(num < 1 or num > total_numbers for num in player_numbers):
                raise ValueError(f"Numbers must be between 1 and {total_numbers}.")

            # Simulate the game
            machine_numbers, correct_count = simulate_lotto(player_numbers)
            results.append((player_numbers, machine_numbers, correct_count))

        # Display results
        result_text = ""
        for i, (player_numbers, machine_numbers, correct_count) in enumerate(results):
            result_text += (f"\nDraw {i+1}:\n"
                            f"Machine numbers: {sorted(machine_numbers)}\n"
                            f"Your numbers: {sorted(player_numbers)}\n"
                            f"Correct numbers: {correct_count}\n")
        messagebox.showinfo("Results", result_text)
        
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the GUI window
root = tk.Tk()
root.title("Lotto Simulator")

# Frame for the bets
bets_frame = tk.Frame(root)
bets_frame.pack(pady=10)

# List to keep track of entry fields for each bet
entries = []

# Function to create new set of entry fields for a new bet
def create_bet_entries():
    frame = tk.Frame(bets_frame)
    frame.pack(pady=5)
    bet_entries = [tk.Entry(frame, width=5) for _ in range(pick_numbers)]
    for entry in bet_entries:
        entry.pack(side=tk.LEFT, padx=5)
    entries.append(bet_entries)
    return bet_entries

# Create initial set of entry fields
create_bet_entries()

# Button to add more bets
def add_bet():
    create_bet_entries()

add_bet_button = tk.Button(root, text="Add Another Bet", command=add_bet)
add_bet_button.pack(pady=10)

# Play button to start the simulation
play_button = tk.Button(root, text="Play", command=on_play)
play_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()

