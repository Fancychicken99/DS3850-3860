import sys

MAXDAYS = 7


def main():
    # Proper list initialization
    sales = []

    print("=" * 40)
    print(" SALES TRACKER SYSTEM")
    print("=" * 40)

    while True:
        # Display menu
        print(f"\nCurrent entries: {len(sales)}/{MAXDAYS} days")
        print("\n1. View all sales")
        print("2. Add daily sale")
        print("3. Calculate total sales")
        print("4. Calculate average sale")
        print("5. Find best day")
        print("6. Find worst day")
        print("7. Show days above average")
        print("8. Exit")
        print("=" * 40)

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "8":
            print("Thank you for using the Sales Tracker System. Goodbye!")
            sys.exit()
        elif choice == "7":
            showDaysAboveAverage(sales)
        elif choice == "6":
            findWorstDay(sales)
        elif choice == "5":
            findBestDay(sales)
        elif choice == "4":
            calculateAverageSale(sales)
        elif choice == "3":
            calculateTotalSales(sales)
        elif choice == "2":
            addDailySale(sales)
        elif choice == "1":
            viewSales(sales)
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


def viewSales(sales):
    # Handle empty list
    if not sales:
        print("No sales data available.")
        return

    print(f"Total entries: {len(sales)}/{MAXDAYS}")
    print("Daily Sales:")
    for i, sale in enumerate(sales, start=1):
        print(f"Day {i}: ${sale:.2f}")


def addDailySale(sales):
    # Prevent adding more than MAXDAYS
    if len(sales) >= MAXDAYS:
        print(f"Maximum number of days ({MAXDAYS}) reached. Cannot add more sales.")
        return

    while True:
        try:
            sale = float(input("Enter daily sale amount: "))
            # Validate positive amounts (must be > 0)
            if sale <= 0:
                print("Sale amount must be a positive number. Please try again.")
                continue
            sales.append(sale)
            print(f"Sale of ${sale:.2f} added successfully.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculateTotalSales(sales):
    # Handle empty list
    if not sales:
        print("No sales data available.")
        return

    total = sum(sales)  # Sum calculation
    print(f"Total Sales: ${total:.2f}")


def calculateAverageSale(sales):
    # Handle empty list
    if not sales:
        print("No sales data available.")
        return

    average = sum(sales) / len(sales)  # Average calculation
    print(f"Average Sale: ${average:.2f}")


def findBestDay(sales):
    # Handle empty list
    if not sales:
        print("No sales data available.")
        return

    bestSale = max(sales)  # Max finding
    dayIndex = sales.index(bestSale) + 1
    print(f"Best Day: Day {dayIndex} with sales of ${bestSale:.2f}")


def findWorstDay(sales):
    # Handle empty list
    if not sales:
        print("No sales data available.")
        return

    worstSale = min(sales)  # Min finding
    dayIndex = sales.index(worstSale) + 1
    print(f"Worst Day: Day {dayIndex} with sales of ${worstSale:.2f}")


def showDaysAboveAverage(sales):
    # Handle empty list
    if not sales:
        print("No sales data available.")
        return

    average = sum(sales) / len(sales)
    print(f"Average Sale: ${average:.2f}")
    print("Days with sales above average:")
    countAbove = 0
    for i, sale in enumerate(sales, start=1):
        if sale > average:
            print(f"Day {i}: ${sale:.2f}")
            countAbove += 1
    if countAbove == 0:
        print("None")
    print(f"Total days above average: {countAbove}")


if __name__ == "__main__":
    main()