"""
Thursday Project 1: Discount Qualification System
Author: Brody Mensonides
Course: DS-3850-001
Purpose: Evaluates customer information and purchasing details 
         to determine eligibility for various discounts.
"""

# Initialize variables
loyaltyDiscount = 0
birthdayDiscount = 0
volumeDiscount = 0
seniorDiscount = 0
firstTimeDiscount = 0
purchaseAmount = 0
yearsMember = 0
customerAge = 0
customerName = ""
isLoyaltyMember = ""
isBirthday = ""
firstTimeCustomer = ""

# Label
print("=" * 40)
print("    DISCOUNT QUALIFICATION SYSTEM")
print("=" * 40)
print()

# Collect customer information
customerName = input("Enter customer name: ")
purchaseAmount = float(input("Enter purchase amount: $"))
isLoyaltyMember = input("Is customer a loyalty member? (yes/no): ").strip().lower()

# Process loyalty membership
while isLoyaltyMember == "yes":
    yearsMember = int(input("Enter number of years as a loyalty member: "))
    purchaseAmount = float(input("Enter customers purchase amount: $"))

    if yearsMember >= 5 and purchaseAmount > 100:
        loyaltyDiscount = 0.20 # 20% discount for 5 or more years and purchase over $100
        break
    elif yearsMember >= 2 and yearsMember <= 4 and purchaseAmount > 100:
        loyaltyDiscount = 0.15 # 15% discount for 2-4 years and purchase over $100
        break
    elif yearsMember == 1 and yearsMember > -1 and purchaseAmount > 150:
        loyaltyDiscount = 0.10 # 10% discount for 0-1 year with filter for negative input and purchase over $150
        break
    else:
        print ("Invalid input for years as a loyalyty member or purchase amount.")
        isLoyaltyMember = input("Are you sure the customer is a loyalty member? (yes/no): ").strip().lower() 
        if isLoyaltyMember == "yes":
            isLoyaltyMember = input("Is the purchase amount over $100 for silver \nand gold members or over $150 for bronze members? (yes/no): ").strip().lower()
            if isLoyaltyMember == "yes":
                continue
            elif isLoyaltyMember == "no":
                print("No loyalty discount can applied.")
                break

# Check for special occasions
isBirthday = input("Is the customer's birthday this month? (yes/no): ").strip().lower()
if isBirthday == "yes":
    birthdayDiscount = 0.05 # 5% birthday discount
firstTimeCustomer = input("Is this the customer's first purchase? (yes/no): ").strip().lower()
if firstTimeCustomer == "yes" and isLoyaltyMember == "no":
    firstTimeDiscount = 0.10 # 10% first-time customer discount

# Check for senior discount
customerAge = int(input("Enter customer's age: "))
if customerAge >= 65:
    seniorDiscount = 0.05 # 5% senior discount

# Check for volume discount if no loyalty discount applied
if loyaltyDiscount == 0:
    if purchaseAmount >= 500:
        volumeDiscount = 0.25 # 25% volume discount for purchases over $500
    elif purchaseAmount >= 300:
        volumeDiscount = 0.15 # 15% volume discount for purchases over $300
    elif purchaseAmount >= 150:
        volumeDiscount = 0.10 # 10% volume discount for purchases over $150