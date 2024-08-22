#Score Grade Program.....

import argparse

# Define the grade function
def calculate_grade(score):
    if score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    else:
        return 'F'

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="Calculate grade based on score")

# Add an argument for score
parser.add_argument("score", type=float, help="The score between 0.0 and 1.0")

# Parse the command-line arguments
args = parser.parse_args()

# Validate the score
while args.score < 0.0 or args.score > 0.9:
    print("Error: Score is out of range.")
    args.score = float(input("Enter a score between 0.0 and 0.9: "))

# Calculate and print the grade
print("Grade:", calculate_grade(args.score))
