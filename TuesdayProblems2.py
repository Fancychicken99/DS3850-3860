# Tuesday Practice Problems 2
# Author: Brody Mensonides
# Course: DS-3850-001

import time
import random

def countdown():
    #Problem 2.1 - Countdown Timer
    print("\n--- Countdown Timer ---")
    seconds = int(input("Enter number of seconds for countdown: "))
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print("Countdown complete!")

def sumCalculator():
    #problem 2.2 - Sum Calculator
    print("\n--- Sum Calculator ---")
    userNumber = int(input("Enter a positive integer: "))
    totalSum = sum(range(1, userNumber + 1))
    print(f"The sum of all integers from 1 to {userNumber} is: {totalSum}\n")

def passwordValidator():
    #problem 2.3 - Password Validator
    print("\n--- Password Validator ---")
    password = str(input("Enter a password: "))
    if (len(password) >= 8 and any(char.isdigit() for char in password)):
        print("Password is valid.\n")
    else:
        print("Password is invalid. It must be at least 8 characters long and include at least 1 digit.\n")

def multiplicationTable():
    #problem 2.4 - Multiplication Table
    print("\n--- Multiplication Table ---")
    number = int(input("Enter an integer to generate its multiplication table: "))
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}\n")

def gradeAnalyzer():
    #problem 2.5 - Grade Analyzer
    print("\n--- Grade Analyzer ---")

    def getClassInfo():
        #collect class information
        numStudents = int(input("Enter number of students in the class: "))
        grades = []
        for i in range(numStudents):
            grade = float(input(f"Enter grade for student {i + 1}: "))
            grades.append(grade)
        return grades

    def analyzeGrades(grades):
        #analyze grades
        averageGrade = sum(grades) / len(grades)
        highestGrade = max(grades)
        lowestGrade = min(grades)
        print(f"\nClass Average: {averageGrade:.2f}")
        print(f"Highest Grade: {highestGrade:.2f}")
        print(f"Lowest Grade: {lowestGrade:.2f}\n")

    userChoice = 'y'
    while userChoice == 'y':
        grades = getClassInfo()
        analyzeGrades(grades)
        userChoice = input("Would you like to go again? y/n: ").lower()
        if userChoice != 'y':
            print("Exiting Grade Analyzer.\n")

def numberGuessingGame():
    #problem 2.6 - Number Guessing Game
    print("\n--- Number Guessing Game ---")
    numberToGuess = random.randint(1,50)
    attempts = 0
    while attempts < 7:
        userGuess = int(input("Guess a number between 1 and 50 you get 7 guesses: "))
        attempts += 1
        if userGuess < numberToGuess:
            print("Too low! Try again.")
        elif userGuess > numberToGuess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {numberToGuess} in {attempts} attempts.\n")
            break
    if attempts >= 7 and userGuess != numberToGuess:
        print(f"Sorry, you've used all 7 attempts. The number was {numberToGuess}.\n")

def evenOddSeparator():
    #problem 2.7 - Even and Odd Number Separator
    print("\n--- Even and Odd Number Separator ---")
    userNumber = int(input("Enter a positive integer to separate even and odd numbers: "))
    numbers = list(range(1, userNumber + 1))
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    print(f"Sum of even numbers: {even_sum}")
    print(f"Sum of odd numbers: {odd_sum}\n")

def compoundInterestCalculator():
    #problem 2.8 - Compound Interest Calculator
    print("\n--- Compound Interest Calculator ---")

    def getInvestmentDetails():
        #collect investment details
        principal = float(input("Enter the principal amount: $"))
        rate = float(input("Enter the annual interest rate (in %): ")) / 100
        years = int(input("Enter the number of years the money is invested: "))
        return principal, rate, years
    
    def calculateCompoundInterest(principal, rate, years):
        #calculate compound interest year by year
        balance = principal
        for year in range(1, years + 1):
            interest_earned = balance * rate
            balance += interest_earned
            print(f"Year {year}: Balance = ${balance:,.2f} (Interest: ${interest_earned:,.2f})")
        
        total_interest = balance - principal
        print(f"\nTotal interest earned: ${total_interest:,.2f}")
        print(f"Final balance: ${balance:,.2f}\n")
    
    principal, rate, years = getInvestmentDetails()
    calculateCompoundInterest(principal, rate, years)

def FizzBuzz():
    #problem 2.9 FizzBuzz
    print("\n--- FizzBuzz ---")
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def primeNumberFinder():
    #problem 2.10 - Prime Number Finder
    print("\n--- Prime Number Finder ---")
    userNumber = int(input("Enter a positive integer to find all prime numbers up to that number: "))
    if userNumber < 2:
        print("Please enter a number greater than or equal to 2.\n")
        return
    primes = []
    for num in range(2, userNumber + 1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    print(f"Prime numbers up to {userNumber}: {primes}\n")
    print(f"Total prime numbers found: {len(primes)}\n")

def main():
    
    userRunning = 'y'
    while userRunning == 'y':
       
        print("Tuesday Practice Problems 2")
        print("Pick a problem to run:")
        print("2.1 - Countdown Timer")
        print("2.2 - Sum Calculator")
        print("2.3 - Password Validator")
        print("2.4 - Multiplication Table")
        print("2.5 - Grade Analyzer")
        print("2.6 - Number Guessing Game")
        print("2.7 - Even and Odd Number Separator")
        print("2.8 - Compound Interest Calculator")
        print("2.9 - FizzBuzz")
        print("2.10 - Prime Number Finder")
        choice = input("Enter the problem number (e.g., 2.1): ")
    
        switch = {
            "2.1": countdown,
            "2.2": sumCalculator,
            "2.3": passwordValidator,
            "2.4": multiplicationTable,
            "2.5": gradeAnalyzer,
            "2.6": numberGuessingGame,
            "2.7": evenOddSeparator,
            "2.8": compoundInterestCalculator,
            "2.9": FizzBuzz,
            "2.10": primeNumberFinder
        }
    
        if choice in switch:
            switch[choice]()
            userRunning = input("Would you like to run another problem? (y/n): ").lower()
        else:
            print("Invalid choice. Please enter a valid problem number.")

if __name__ == "__main__":
    main()
    
