# DS 3850: Business Applications Development
# Brody Mensonides
# Tuesday Problems 3

import sys


# Problem 3.1: Email Validator
def emailValidator():
    # Function to validate an email address
    email = input("Enter email: ").strip()
    emailLower = email.lower()

    # Validate email structure
    if emailLower.count("@") != 1:
        print("Invalid email (missing @)")
    elif "." not in emailLower.split("@")[1]:
        print("Invalid email (missing . after @)")
    elif " " in emailLower:
        print("Invalid email (contains spaces)")
    else:
        print(f"Valid email: {emailLower}")


# Problem 3.2: Word Counter
def wordCounter():
    # Function to count words and characters in a sentence
    sentence = input("Enter a sentence: ").strip()
    words = sentence.split()
    chars = sentence.replace(" ", "")

    # Print counts and transformations
    print(f"Total words: {len(words)}")
    print(f"Total characters: {len(chars)}")
    print(f"Uppercase: {sentence.upper()}")
    print(f"Lowercase: {sentence.lower()}")


# Problem 3.3: Name Formatter
def nameFormatter():
    # Function to format a name into "Last, First M." format
    name = input("Enter name: ").strip()
    parts = name.split()

    if len(parts) < 2:
        print("Please enter at least first and last name")
        return

    lastName = parts[-1].capitalize()
    firstName = parts[0].capitalize()
    middleInitial = ""

    if len(parts) > 2:
        middleInitial = f" {parts[1][0].upper()}."

    print(f"Formatted: {lastName}, {firstName}{middleInitial}")


# Problem 3.4: Phone Number Formatter
def phoneFormatter():
    # Function to format a phone number
    phone = input("Enter phone: ").strip()
    digits = "".join(c for c in phone if c.isdigit())

    if len(digits) != 10:
        print("Invalid phone number (must be 10 digits)")
        return

    formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    print(f"Formatted: {formatted}")


# Problem 3.5: Student Grade Book
def gradeBook():
    # Function to manage a grade book for students
    grades = {}

    while True:
        name = input("Enter student name (or 'done'): ").strip()
        if name.lower() == "done":
            break
        grade = float(input("Enter grade: "))
        grades[name] = grade

    print("GRADE BOOK")
    for name, grade in grades.items():
        print(f"{name}: {grade}")

    avg = sum(grades.values()) / len(grades)
    highest = max(grades, key=grades.get)
    lowest = min(grades, key=grades.get)

    # Print statistics
    print(f"Class Average: {avg:.2f}")
    print(f"Highest: {highest} ({grades[highest]})")
    print(f"Lowest: {lowest} ({grades[lowest]})")


# Problem 3.6: Product Inventory
def productInventory():
    # Function to manage a product inventory
    inventory = {}

    while True:
        # Display menu options
        print("1. View all products")
        print("2. Add product")
        print("3. Update quantity")
        print("4. Search product")
        print("5. Exit")
        choice = input("Choice: ")

        if choice == "1":
            print("INVENTORY")
            for product, qty in inventory.items():
                print(f"{product}: {qty} units")
        elif choice == "2":
            name = input("Product name: ")
            qty = int(input("Quantity: "))
            inventory[name] = qty
            print(f"Added {name} ({qty} units)")
        elif choice == "3":
            name = input("Product name: ")
            if name in inventory:
                qty = int(input("New quantity: "))
                inventory[name] = qty
                print(f"Updated {name} to {qty} units")
        elif choice == "4":
            name = input("Search for: ")
            if name in inventory:
                print(f"Found: {name} ({inventory[name]} units)")
            else:
                print(f"Not found: {name}")
        elif choice == "5":
            return


# Problem 3.7: Text Statistics
def textStatistics():
    # Function to analyze text statistics
    text = input("Enter text: ").strip()
    words = text.split()
    sentences = text.count(".") + text.count("!") + text.count("?")

    wordFreq = {}
    for word in words:
        cleanWord = word.lower().strip(".,!?;:")
        wordFreq[cleanWord] = wordFreq.get(cleanWord, 0) + 1

    # Print statistics
    print(f"Total words: {len(words)}")
    print(f"Total sentences: {max(sentences, 1)}")
    print(f"Average words per sentence: {len(words) / max(sentences, 1):.1f}")
    print("Word Frequency:")
    for word, freq in sorted(wordFreq.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {freq}")

    mostCommon = max(wordFreq, key=wordFreq.get)
    print(f"Most common word: {mostCommon} ({wordFreq[mostCommon]} times)")


# Problem 3.8: Contact Manager
def contactManager():
    # Function to manage contacts
    contacts = []

    while True:
        # Display menu options
        print("1. View all contacts")
        print("2. Add contact")
        print("3. Search by name")
        print("4. Delete contact")
        print("5. Exit")
        choice = input("Choice: ")

        if choice == "1":
            print("ALL CONTACTS")
            for contact in contacts:
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
        elif choice == "2":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            contacts.append({"name": name, "phone": phone, "email": email})
            print("Contact added")
        elif choice == "3":
            search = input("Search name: ")
            for contact in contacts:
                if search.lower() in contact["name"].lower():
                    print(f"Found: {contact['name']} ({contact['phone']})")
        elif choice == "4":
            name = input("Contact name: ")
            contacts = [c for c in contacts if c["name"].lower() != name.lower()]
            print("Contact deleted")
        elif choice == "5":
            return


# Problem 3.9: Employee Database
def employeeDatabase():
    # Function to manage employee database
    employees = []

    while True:
        # Display menu options
        print("1. View all employees")
        print("2. Add employee")
        print("3. Search by ID")
        print("4. Calculate total payroll")
        print("5. Average salary by department")
        print("6. Highest paid employee")
        print("7. Exit")
        choice = input("Choice: ")

        if choice == "1":
            print("ALL EMPLOYEES")
            for emp in employees:
                print(
                    f"{emp['id']} - {emp['name']} ({emp['department']}) ${emp['salary']:,}"
                )
        elif choice == "2":
            empId = input("ID: ")
            name = input("Name: ")
            dept = input("Department: ")
            salary = int(input("Salary: "))
            employees.append(
                {"id": empId, "name": name, "department": dept, "salary": salary}
            )
            print("Employee added")
        elif choice == "3":
            empId = input("Search ID: ")
            for emp in employees:
                if emp["id"] == empId:
                    print(
                        f"Found: {emp['name']} ({emp['department']}) ${emp['salary']:,}"
                    )
        elif choice == "4":
            total = sum(emp["salary"] for emp in employees)
            print(f"Total Payroll: ${total:,}")
        elif choice == "5":
            dept = input("Department: ")
            deptSalaries = [
                emp["salary"] for emp in employees if emp["department"] == dept
            ]
            if deptSalaries:
                avg = sum(deptSalaries) / len(deptSalaries)
                print(f"{dept} Department Average: ${avg:,.0f}")
        elif choice == "6":
            highest = max(employees, key=lambda x: x["salary"])
            print(
                f"Highest Paid: {highest['name']} ({highest['department']}, ${highest['salary']:,})"
            )
        elif choice == "7":
            return


# Problem 3.10: CSV Parser
def csvParser():
    # Function to parse CSV data
    print("Enter CSV data (end with empty line):")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)

    headers = lines[0].split(",")
    data = []

    for line in lines[1:]:
        values = line.split(",")
        row = {}
        for i, header in enumerate(headers):
            try:
                row[header.strip()] = int(values[i].strip())
            except ValueError:
                row[header.strip()] = values[i].strip()
        data.append(row)

    print("PARSED DATA")
    for emp in data:
        print(f"{emp['name']} {emp['age']} {emp['department']} ${int(emp['salary']):,}")

    # Calculate statistics
    depts = set(emp["department"] for emp in data)
    salaries = [emp["salary"] for emp in data]
    ages = [emp["age"] for emp in data]

    # Print statistics
    print("STATISTICS")
    print(f"Departments: {', '.join(sorted(depts))}")
    print(f"Salary Range: ${min(salaries):,} - ${max(salaries):,}")
    print(f"Average Age: {sum(ages) / len(ages):.2f}")


def main():
    # Main menu function to select problems
    problems = {
        "3.1": emailValidator,
        "3.2": wordCounter,
        "3.3": nameFormatter,
        "3.4": phoneFormatter,
        "3.5": gradeBook,
        "3.6": productInventory,
        "3.7": textStatistics,
        "3.8": contactManager,
        "3.9": employeeDatabase,
        "3.10": csvParser,
    }

    while True:
        choice = input("Select problem (3.1-3.10) or 'q' to quit: ")
        if choice.lower() == "q":
            sys.exit()
        if choice in problems:
            problems[choice]()


if __name__ == "__main__":
    main()
