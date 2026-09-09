import random

# Computer choice
computer = random.choice([-1, 0, 1])

# User input
youstr = input("Enter your choice (stone), (paper), (seyser): ").lower()

# Dictionary
youDict = {
    "stone": -1,
    "paper": 0,
    "seyser": 1
}

reverseDict = {
    -1: "Stone",
    0: "Paper",
    1: "Seyser"
}

# Check valid input
if youstr not in youDict:
    print("Invalid Choice!")
else:
    you = youDict[youstr]

    print(f"You chose {reverseDict[you]}")
    print(f"Computer chose :{reverseDict[computer]}")

    if computer == you:
        print("Match Draw!")

    elif (computer == -1 and you == 0):      # Stone vs Paper
        print("You Win!")

    elif (computer == 0 and you == 1):       # Paper vs Scissors
        print("You Win!")

    elif (computer == 1 and you == -1):      # Scissors vs Stone
        print("You Win!")

    else:
        print("You Lose!")