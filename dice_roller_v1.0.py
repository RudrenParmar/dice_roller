import random

# Dice Roller - Version 1.0

num_dice = int(input("Enter the number of dice: "))
num_faces = int(input("Enter the number of die faces: "))

min_val = num_dice * 1
max_val = num_dice * num_faces

result = random.randint(min_val, max_val)

print(f"You rolled: {result}")

if result == max_val:
    print("Congratulations! You rolled the maximum value!")
