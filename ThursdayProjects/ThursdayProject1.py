# Thursday Project 1: Discount Qualification System
# Author: Brody Mensonides
# Course: DS-3850-001
# Purpose: Evaluates customer information and purchasing details to determine eligibility for various discounts.

import sys
import time

def getCustomerInfo():
    # Collect basic customer information.
    print("=" * 40)
    print("    DISCOUNT QUALIFICATION SYSTEM")
    print("=" * 40)
    print()
    
    customerName = input("Enter customer name: ")
    purchaseAmount = float(input("Enter purchase amount: $"))
    return customerName, purchaseAmount

def processLoyaltyDiscount(purchaseAmount):
    # Process loyalty membership and calculate discount.
    isLoyaltyMember = input("Is the customer a loyalty member? (yes/no): ").strip().lower()
    loyaltyDiscount = 0
    
    while isLoyaltyMember == "yes":
        yearsMember = int(input("Enter number of years as a loyalty member: "))
        
        if yearsMember >= 5 and purchaseAmount >= 100:
            loyaltyDiscount = 0.20
            print("20 percent Loyalty discount applied.")
            break
        elif yearsMember >= 2 and yearsMember <= 4 and purchaseAmount >= 100:
            loyaltyDiscount = 0.15
            print("15 percent Loyalty discount applied.")
            break
        elif yearsMember == 1 and yearsMember > -1 and purchaseAmount >= 150:
            loyaltyDiscount = 0.10
            print("10 percent Loyalty discount applied.")
            break
        else:
            print("Invalid input for years as a loyalty member or purchase amount.")
            isLoyaltyMember = input("Are you sure the customer is a loyalty member? (yes/no): ").strip().lower()
            if isLoyaltyMember == "yes":
                isLoyaltyMember = input("Is the purchase amount over $100 for silver \nand gold members or over $150 for bronze members? (yes/no): ").strip().lower()
                if isLoyaltyMember == "no":
                    print("No loyalty discount can applied.")
                    loyaltyDiscount = 0
                    break
            else:
                loyaltyDiscount = 0
                break
    
    return loyaltyDiscount

def processOccasionDiscounts(isLoyaltyMember):
    # Process birthday and first-time customer discounts.
    birthdayDiscount = 0
    firstTimeDiscount = 0
    
    isBirthday = input("Is the customer's birthday this month? (yes/no): ").strip().lower()
    firstTimeCustomer = input("Is this the customer's first purchase? (yes/no): ").strip().lower()
    
    if isBirthday == "yes":
        birthdayDiscount = 0.05
        print("5 percent Birthday discount applied.")
    if firstTimeCustomer == "yes" and isLoyaltyMember == "no":
        firstTimeDiscount = 0.10
        print("10 percent First-time customer discount applied.")
    elif firstTimeCustomer == "yes" and isLoyaltyMember == "yes":
        firstTimeDiscount = 0
        print("No first-time customer discount can be applied for loyalty members.")
    elif isBirthday == "no" and firstTimeCustomer == "no":
        print("No occasion-based discounts can be applied.")
    
    return birthdayDiscount, firstTimeDiscount

def processSeniorDiscount():
    # Check for senior discount.
    customerAge = int(input("Enter customer's age: "))
    seniorDiscount = 0
    
    if customerAge >= 65:
        seniorDiscount = 0.05
        print("5 percent Senior discount applied.")
    else:
        print("No senior discount can be applied.")
    
    return seniorDiscount

def processVolumeDiscount(loyaltyDiscount, purchaseAmount):
    # Check for volume discount.
    volumeDiscount = 0
    
    if loyaltyDiscount == 0:
        if purchaseAmount >= 500:
            volumeDiscount = 0.25
            print("25 percent Volume discount applied.")
        elif purchaseAmount >= 300:
            volumeDiscount = 0.15
            print("15 percent Volume discount applied.")
        elif purchaseAmount >= 150:
            volumeDiscount = 0.10
            print("10 percent Volume discount applied.")
    elif loyaltyDiscount > 0:
        print("No volume discount can be applied.")
    
    return volumeDiscount

def calculateFinalPrice(purchaseAmount, loyaltyDiscount, birthdayDiscount, volumeDiscount, seniorDiscount, firstTimeDiscount):
    # Calculate total discount and final price.
    totalDiscount = loyaltyDiscount + birthdayDiscount + volumeDiscount + seniorDiscount + firstTimeDiscount
    
    if totalDiscount > 0.35:
        totalDiscount = 0.35
        print("Maximum discount of 35 exceeded 35 percent discount applied.")
    
    finalDiscount = purchaseAmount * totalDiscount
    finalPrice = purchaseAmount - finalDiscount
    
    return totalDiscount, finalDiscount, finalPrice

def displayResults(customerName, purchaseAmount, loyaltyDiscount, birthdayDiscount, firstTimeDiscount, seniorDiscount, volumeDiscount, totalDiscount, finalDiscount, finalPrice):
    # Display discount summary.
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

def main():
    # Main function to run the discount qualification system.
    continueProcessing = "yes"
    
    while continueProcessing.lower() == "yes":
        customerName, purchaseAmount = getCustomerInfo()
        loyaltyDiscount = processLoyaltyDiscount(purchaseAmount)
        birthdayDiscount, firstTimeDiscount = processOccasionDiscounts(loyaltyDiscount)
        seniorDiscount = processSeniorDiscount()
        
        time.sleep(1.5)
        
        volumeDiscount = processVolumeDiscount(loyaltyDiscount, purchaseAmount)
        
        time.sleep(1.5)
        
        totalDiscount, finalDiscount, finalPrice = calculateFinalPrice(purchaseAmount, loyaltyDiscount, birthdayDiscount, volumeDiscount, seniorDiscount, firstTimeDiscount)
        
        time.sleep(1.5)
        
        displayResults(customerName, purchaseAmount, loyaltyDiscount, birthdayDiscount, firstTimeDiscount, seniorDiscount, volumeDiscount, totalDiscount, finalDiscount, finalPrice)
        
        print("Thank you for using the Discount Qualification System!")
        continueProcessing = input("Would you like to process another customer? (yes/no): ")
        print("=" * 40)
    
    sys.exit(0)

if __name__ == "__main__":
    main()
