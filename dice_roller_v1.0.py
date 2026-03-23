import random

# Dice Roller - Version 1.1

play_again = "yes"

while play_again.lower() == "yes":

    # Re-prompt if zero or invalid
    num_dice = 0
    while num_dice == 0:
        num_dice = int(input("Enter the number of dice (non-zero): "))
        if num_dice == 0:
            print("Number of dice cannot be zero. Try again.")

    num_faces = 0
    while num_faces == 0:
        num_faces = int(input("Enter the number of die faces (non-zero): "))
        if num_faces == 0:
            print("Number of die faces cannot be zero. Try again.")

    min_val = num_dice * 1
    max_val = num_dice * num_faces

    result = random.randint(min_val, max_val)

    print(f"You rolled: {result}")

    if result == max_val:
        print("Congratulations! You rolled the maximum value!")

    play_again = input("Roll again? (yes/no): ")

print("Thanks for playing!")
