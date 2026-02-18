# Inventory Management System
# DS 3850 - Thursday Project 3
# Your Name

inventory = []

# Main menu display function
def displayMenu():
    print("\n" + "="*40)
    print(" INVENTORY MANAGEMENT SYSTEM")
    print("="*40)
    print("1. View all products")
    print("2. Add new product")
    print("3. Update quantity")
    print("4. Search product")
    print("5. Remove product")
    print("6. Calculate inventory value")
    print("7. Low stock alert")
    print("8. Exit")
    print("="*40)

# Display all products in formatted table
def viewAllProducts(inventory):
    if not inventory:
        print("\nInventory is empty!")
        return
    
    print("\n" + "-"*80)
    print(f"{'Name':<20} {'Category':<15} {'Quantity':<10} {'Price':<10}")
    print("-"*80)
    for product in inventory:
        print(f"{product['name']:<20} {product['category']:<15} {product['quantity']:<10} ${product['price']:<9.2f}")
    print("-"*80)

# Add new product to inventory
def addProduct(inventory):
    name = input("Enter product name: ").strip()
    
    # Check for empty name
    if not name:
        print("Product name cannot be empty!")
        return
    
    # Check for duplicates
    for product in inventory:
        if product['name'].lower() == name.lower():
            print("Product already exists in inventory!")
            return
    
    category = input("Enter category: ").strip()
    
    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity must be a positive integer!")
            return
    except ValueError:
        print("Invalid quantity entered!")
        return
    
    try:
        price = float(input("Enter price: "))
        if price <= 0:
            print("Price must be a positive number!")
            return
    except ValueError:
        print("Invalid price entered!")
        return
    
    newProduct = {
        "name": name,
        "category": category,
        "quantity": quantity,
        "price": price
    }
    
    inventory.append(newProduct)
    print(f"Product '{name}' added successfully!")

# Update quantity for existing product
def updateQuantity(inventory):
    if not inventory:
        print("Inventory is empty!")
        return
    
    productName = input("Enter product name to update: ").strip()
    
    for product in inventory:
        if product['name'].lower() == productName.lower():
            try:
                newQuantity = int(input("Enter new quantity: "))
                if newQuantity < 0:
                    print("Quantity cannot be negative!")
                    return
                product['quantity'] = newQuantity
                print(f"Quantity updated to {newQuantity}!")
                return
            except ValueError:
                print("Invalid quantity entered!")
                return
    
    print("Product not found!")

# Search and display product by name
def searchProduct(inventory):
    if not inventory:
        print("Inventory is empty!")
        return
    
    productName = input("Enter product name to search: ").strip()
    
    for product in inventory:
        if product['name'].lower() == productName.lower():
            print("\n" + "-"*60)
            print(f"Name: {product['name']}")
            print(f"Category: {product['category']}")
            print(f"Quantity: {product['quantity']}")
            print(f"Price: ${product['price']:.2f}")
            print("-"*60)
            return
    
    print("Product not found!")

# Remove product from inventory
def removeProduct(inventory):
    if not inventory:
        print("Inventory is empty!")
        return
    
    productName = input("Enter product name to remove: ").strip()
    
    for i, product in enumerate(inventory):
        if product['name'].lower() == productName.lower():
            inventory.pop(i)
            print(f"Product '{productName}' removed successfully!")
            return
    
    print("Product not found!")

# Calculate total value of all inventory
def calculateInventoryValue(inventory):
    if not inventory:
        print("Inventory is empty!")
        return
    
    totalValue = sum(product['quantity'] * product['price'] for product in inventory)
    print(f"\nTotal inventory value: ${totalValue:.2f}")

# Display products below threshold quantity
def lowStockAlert(inventory, threshold=5):
    if not inventory:
        print("Inventory is empty!")
        return
    
    lowStockItems = [product for product in inventory if product['quantity'] < threshold]
    
    if not lowStockItems:
        print(f"\nNo products with stock below {threshold} units!")
        return
    
    print(f"\n--- LOW STOCK ALERT (Below {threshold} units) ---")
    for product in lowStockItems:
        print(f"{product['name']}: {product['quantity']} units")

# Main program loop
while True:
    displayMenu()
    choice = input("\nChoice: ").strip()
    
    if choice == "1":
        viewAllProducts(inventory)
    elif choice == "2":
        addProduct(inventory)
    elif choice == "3":
        updateQuantity(inventory)
    elif choice == "4":
        searchProduct(inventory)
    elif choice == "5":
        removeProduct(inventory)
    elif choice == "6":
        calculateInventoryValue(inventory)
    elif choice == "7":
        lowStockAlert(inventory)
    elif choice == "8":
        print("\nThank you for using Inventory Manager!")
        break
    else:
        print("Invalid choice! Please select 1-8.")