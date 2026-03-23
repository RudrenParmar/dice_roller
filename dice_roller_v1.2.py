import random

# Dice Roller - Version 1.2


def get_numdice():
    """Prompts user for number of dice. Re-prompts if value is less than 1. Returns valid input."""
    num_dice = 0
    while num_dice < 1:
        num_dice = int(input("Enter the number of dice (minimum 1): "))
        if num_dice < 1:
            print("Number of dice must be at least 1. Try again.")
    return num_dice


def get_diefaces():
    """Prompts user for number of die faces. Re-prompts if value is less than 1. Returns valid input."""
    num_faces = 0
    while num_faces < 1:
        num_faces = int(input("Enter the number of die faces (minimum 1): "))
        if num_faces < 1:
            print("Number of die faces must be at least 1. Try again.")
    return num_faces


def roll_dice(num_dice, num_faces):
    """Takes number of dice and number of faces. Returns result of the dice roll."""
    min_val = num_dice * 1
    max_val = num_dice * num_faces
    return random.randint(min_val, max_val)


def is_max_score(result, max_val):
    """Takes result and maximum possible value. Returns True if result equals max, False otherwise."""
    if result == max_val:
        return True
    else:
        return False


# --- Main Program ---

play_again = "yes"

while play_again.lower() == "yes":

    num_faces = get_diefaces()
    num_dice = get_numdice()

    max_val = num_dice * num_faces
    result = roll_dice(num_dice, num_faces)

    print(f"You rolled: {result}")

    if is_max_score(result, max_val):
        print("Congratulations! You rolled the maximum value!")

    play_again = input("Roll again? (yes/no): ")

print("Thanks for playing!")
