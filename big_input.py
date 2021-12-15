# big_input.py
# Author: Levi Graham
# Date: 12/12/21
# Course: CSCI 262: Algorithms
# Purpose: To programmatically generate the large input for the 
#          final project.
# Modification Log:
#   2021.12.12 - Wrote the script.

# Import the randint() method from the random library.
from random import randint

# Constants
TEXT = "Lorem ipsum dolor sit amet consectetur adipiscing elit. Nunc pellentesque magna posuere dolor ultrices aliquam Etiam vitae ipsum enim Nunc consequat velit eu tortor".split(" ")
HASH = "ACCESS AFFECT ANIMAL ATTACK BUDGET BLESSED CHOICE DANGER EFFORT ENERGY FABRIC REALITY GLOBAL LISTEN MASTER OFFICE NATURE PROFIT RANDOM REPEAT SAFETY SIGNED TALENT TRAVEL WEALTH WRITER".split(" ")
LENGTH = [50, 100, 200, 500, 1000, 2000, 5000]

# For the lengths given, create a file for each one.
for length in LENGTH:
    # Create the file.
    with open(f"long_input_{length}.csv", "w") as file:
        # Add an accumulator for the generated lines.
        lines = []
        # Generate a line for the length. 
        for i in range(length):
            random_hash = randint(0, len(HASH) - 1)
            random_text = randint(1, len(TEXT) - 1)
            text = " ".join(TEXT[:random_text])
            lines.append(f"{HASH[random_hash]},{text}\n")

        # Write the accumulated lines to the file
        file.writelines(lines)
    # Print out that the file was successfully created.
    print(f"File created {length}")