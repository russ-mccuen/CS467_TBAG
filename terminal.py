import os
import time


def menu():
    # Display game menu
    time.sleep(1.5)
    clear_screen()
    print("\n But an instant . . . \n")
    print(" 1. Start game")
    print(" 2. Load game")
    print(" 3. Quit\n")


def loading_screen():
    # Display loading screen animation
    print(" Loading game...")
    for i in range(1, 11):
        time.sleep(0.5)
        print(" Loading" + "." * i)
    print(" Game loaded!")


def start_screen():
    while True:
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            print("Starting game...")
            clear_screen()
            return True
        elif choice == "2":
            if os.path.exists('savedata.json'):
                print("Loading game...")
                return choice
            else:
                print("Save data not found.")
                menu()
                continue
        elif choice == "3":
            print("Exiting game...")
            time.sleep(1)
            clear_screen()
            break
        else:
            print("Invalid input. Please enter a number between 1 and 3.")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def newline():
    print('\n')
