import random  
import math    
from datetime import datetime  

def problem_1():
    """Personal Info Display"""
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    city = input("Enter your city: ")
    had_birthday = input("Have you had your birthday this year? (yes/no): ").strip().lower()
    
    current_date = datetime.now()
    birth_year = current_date.year - age
    
    # Adjust birth year based on whether the user has had their birthday this year
    if had_birthday != 'yes':
        birth_year -= 1
    
    print(f"\n--- Personal Info ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Birth Year: {birth_year}\n")

def problem_2():
    """Simple Calculator"""
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    total = num1 + num2
    difference = num1 - num2
    
    print(f"\n--- Calculator Results ---")
    print(f"Number 1: {num1:.2f}")
    print(f"Number 2: {num2:.2f}")
    print(f"Sum: {total:.2f}")
    print(f"Difference: {difference:.2f}\n")

def problem_3():
    """Random Number Guesser"""
    secret_number = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))
    
    print(f"\n--- Random Number Guesser ---")
    print(f"The number was: {secret_number}")
    print(f"Your guess was: {guess}\n")

def problem_4():
    """Circle Calculator"""
    radius = float(input("Enter the radius of a circle: "))
    area = math.pi * (radius ** 2)
    
    print(f"\n--- Circle Calculator ---")
    print(f"Radius: {radius:.2f}")
    print(f"Area: {area:.2f}\n")

def display_menu():
    """Display the menu and return user choice"""
    print("=" * 30)
    print("PRACTICE PROBLEMS MENU")
    print("=" * 30)
    print("1. Personal Info Display")
    print("2. Simple Calculator")
    print("3. Random Number Guesser")
    print("4. Circle Calculator")
    print("5. Exit")
    print("=" * 30)
    return input("Select a problem (1-5): ")

def main():
    """Main function to run the menu loop"""
    problems = {
        "1": problem_1,
        "2": problem_2,
        "3": problem_3,
        "4": problem_4,
    }
    
    choice = display_menu()
    
    while choice != "5":
        if choice in problems:
            problems[choice]()
        else:
            print("Invalid choice. Please try again.\n")
        
        choice = display_menu()
    
    print("Goodbye!")

if __name__ == "__main__":
    main()
