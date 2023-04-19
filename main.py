import time

# Display loading screen animation
print("Loading game...")
for i in range(1, 11):
    time.sleep(0.5)
    print("Loading" + "." * i)
print("Game loaded!")

# Display game menu
print("Welcome to Adam and Russ' Awesome Text-Based Adventure Game!")
print("1. Start game")
print("2. Options")
print("3. Quit")

# Prompt user for input
while True:
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        print("Starting game...")
        # TODO: Add game code here
        break
    elif choice == "2":
        print("Options menu...")
        # TODO: Add options code here
        break
    elif choice == "3":
        print("Exiting game...")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 3.")
