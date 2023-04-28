import os
import time

def menu():
    # Display game menu
    time.sleep(1.5)
    clear_screen()
    print("Welcome to Adam and Russ' Awesome Text-Based Adventure Game!")
    print("1. Start game")
    print("2. Options")
    print("3. Quit")


def start_screen():
    while True:
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            print("Starting game...")
            clear_screen()
            return True
        elif choice == "2":
            print("Options menu...")
            # TODO: Add options code here
            break
        elif choice == "3":
            print("Exiting game...")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 3.")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')