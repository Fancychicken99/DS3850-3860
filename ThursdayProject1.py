"""
Thursday Project 1: Discount Qualification System
Author: Brody Mensonides
Course: DS-3850-001
Purpose: Evaluates customer information and purchasing details \nto determine eligibility for various discounts.
"""

import sys

# Initialize variables
loyaltyDiscount = 0
birthdayDiscount = 0
volumeDiscount = 0
seniorDiscount = 0
firstTimeDiscount = 0
purchaseAmount = 0
yearsMember = 0
customerAge = 0
totalDiscount = 0
finalDiscount = 0
finalPrice = 0
customerName = ""
isLoyaltyMember = ""
isBirthday = ""
firstTimeCustomer = ""
continueProcessing = "yes"

while continueProcessing.lower() == "yes":

    # Label
    print("=" * 40)
    print("    DISCOUNT QUALIFICATION SYSTEM")
    print("=" * 40)
    print()

    # Collect customer information
    customerName = input("Enter customer name: ")
    purchaseAmount = float(input("Enter purchase amount: $"))
    isLoyaltyMember = input(
        "Is the customer a loyalty member? (yes/no): ").strip().lower()

    # Process loyalty membership
    while isLoyaltyMember == "yes":
        yearsMember = int(input("Enter number of years as a loyalty member: "))
        purchaseAmount = float(input("Enter customers purchase amount: $"))

        if yearsMember >= 5 and purchaseAmount > 100:
            loyaltyDiscount = 0.20  # 20% discount for 5 or more years and purchase over $100
            print("20 percent Loyalty discount applied.")
            break
        elif yearsMember >= 2 and yearsMember <= 4 and purchaseAmount > 100:
            loyaltyDiscount = 0.15  # 15% discount for 2-4 years and purchase over $100
            print("15 percent Loyalty discount applied.")
            break
        elif yearsMember == 1 and yearsMember > -1 and purchaseAmount > 150:

            # 10% discount for 0-1 year with filter for negative input and purchase over $150
            loyaltyDiscount = 0.10
            print("10 percent Loyalty discount applied.")
            break
        else:
            print("Invalid input for years as a loyalyty member or purchase amount.")
            isLoyaltyMember = (
                input("Are you sure the customer is a loyalty member? (yes/no): ")
                .strip()
                .lower()
            )
            if isLoyaltyMember == "yes":
                isLoyaltyMember = (
                    input(
                        "Is the purchase amount over $100 for silver \nand gold members or over $150 for bronze members? (yes/no): "
                    )
                    .strip()
                    .lower()
                )
                if isLoyaltyMember == "yes":
                    continue
                elif isLoyaltyMember == "no":
                    print("No loyalty discount can applied.")
                    loyaltyDiscount = 0
                    break

    # Check for special occasions
    isBirthday = input(
        "Is the customer's birthday this month? (yes/no): ").strip().lower()
    firstTimeCustomer = (
        input("Is this the customer's first purchase? (yes/no): ").strip().lower())
    if isBirthday == "yes":
        birthdayDiscount = 0.05  # 5% birthday discount
        print("5 percent Birthday discount applied.")
    if firstTimeCustomer == "yes" and isLoyaltyMember == "no":
        firstTimeDiscount = 0.10  # 10% first-time customer discount
        print("10 percent First-time customer discount applied.")
    elif isBirthday == "no" and firstTimeCustomer == "no":
        print("No occasion-based discounts can be applied.")
    # Check for senior discount
    customerAge = int(input("Enter customer's age: "))
    if customerAge >= 65:
        seniorDiscount = 0.05  # 5% senior discount
        print("5 percent Senior discount applied.")

    # Check for volume discount if no loyalty discount applied
    if loyaltyDiscount == 0:
        if purchaseAmount >= 500:
            volumeDiscount = 0.25  # 25% volume discount for purchases over $500
            print("25 percent Volume discount applied.")
        elif purchaseAmount >= 300:
            volumeDiscount = 0.15  # 15% volume discount for purchases over $300
            print("15 percent Volume discount applied.")
        elif purchaseAmount >= 150:
            volumeDiscount = 0.10  # 10% volume discount for purchases over $150
            print("10 percent Volume discount applied.")

    # Calculate total discount
    totalDiscount = (
        loyaltyDiscount
        + birthdayDiscount
        + volumeDiscount
        + seniorDiscount
        + firstTimeDiscount
    )

    # Enforce 35% maximum discount
    if totalDiscount > 0.35:
        totalDiscount = 0.35
        print("Maximum discount of 35 exceeded 35 percent discount applied.")

    # Calculate final price
    finalDiscount = purchaseAmount * (totalDiscount / 100)
    finalPrice = purchaseAmount - finalDiscount

    # Display results
    print()
    print("=" * 40)
    print("       DISCOUNT SUMMARY FOR", customerName.upper())
    print("=" * 40)

    print(f"Customer Name: {customerName}")
    print(f"Original Purchase Amount: ${purchaseAmount:.2f}\n\n")
    print("Discounts Applied:")
    if loyaltyDiscount > 0:
        print(f"Loyalty Discount: {loyaltyDiscount * 100:.0f}%")
    if birthdayDiscount > 0:
        print(f"Birthday Discount: {birthdayDiscount * 100:.0f}%")
    if firstTimeDiscount > 0:
        print(f"First-Time Customer Discount: {firstTimeDiscount * 100:.0f}%")
    if seniorDiscount > 0:
        print(f"Senior Discount: {seniorDiscount * 100:.0f}%")
    if volumeDiscount > 0:
        print(f"Volume Discount: {volumeDiscount * 100:.0f}%")
    print("-" * 20)
    print(f"Total Discount: {totalDiscount * 100:.0f}%")
    print(f"Savings Amount: ${finalDiscount:.2f}")
    print(f"Final Price after Discounts: ${finalPrice:.2f}\n\n")

    print("=" * 40)
    print("Thank you for using the Discount Qualification System!")
    continueProcessing = input(
        "Would you like to process another customer? (yes/no)")
    print("=" * 40)

sys.exit(0)
