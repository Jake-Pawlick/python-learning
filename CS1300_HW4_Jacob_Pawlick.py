# Problem 1: Movie Ticket Pricing
'''
age = int(input("Enter your age: "))
matinee_input = input("Is this a matinee showing? (yes/no): ").strip().lower()
is_matinee = True if matinee_input == "yes" else False
if age < 0:
    print("Error: Age cannot be negative.")
else:
    if age < 13:
        group = "Child"
        if is_matinee:
            price = 6.00
        else:
            price = 8.00
    elif age <= 17:
        group = "Teen"
        if is_matinee:
            price = 7.00
        else:
            price = 10.00
    elif age <= 64:
        group = "Adult"
        if is_matinee:
            price = 8.00
        else:
            price = 13.00
    else:
        group = "Senior"
        if is_matinee:
            price = 6.00
        else:
            price = 7.00
    print(f"\nAge group: {group}")
    print(f"Ticket price: ${price:.2f}")
'''
# Problem 2: Input Validator
'''
errors = []
student_id = input("Enter student ID: ")
name = input("Enter full name: ")
age_input = input("Enter age: ")
major = input("Enter major: ")
if len(student_id) != 8:
    errors.append(f"Student ID must be exactly 8 characters (got {len(student_id)})")
if not student_id or not student_id[0].isalpha():
    errors.append("Student ID must start with a letter")
if len(student_id) >= 2 and not student_id[1:].isdigit():
    errors.append("Student ID must have 7 digits after the first letter")
if len(name.strip()) < 2:
    errors.append("Name cannot be empty")
try:
    age = int(age_input)
    if age < 16 or age > 99:
        errors.append("Age must be between 16 and 99")
except:
    errors.append("Age must be a valid integer")
valid_majors = ["CS", "IT", "CE", "DS"]
if major.upper() not in valid_majors:
    errors.append(f"Major must be one of: CS, IT, CE, DS (got {major})")
if len(errors) == 0:
    print("\n✓ Profile created successfully!")
    print(f"Student ID: {student_id}")
    print(f"Name:       {name}")
    print(f"Age:        {age}")
    print(f"Major:      {major.upper()}")
else:
    print("\nX Profile has errors:")
    for e in errors:
        print(f"- {e}")
'''
# Problem 3: Campus Café Menu
'''
print("==============================")
print("     CAMPUS CAFÉ ORDER SYSTEM")
print("==============================")
print("1. Coffee     - $3.50")
print("2. Sandwich   - $6.00")
print("3. Salad      - $5.50")
print("4. Combo      - $8.00")
print("5. Exit")
print("==============================")

choice = input("Enter your choice (1-5): ").strip()

price = 0
item_name = ""

if choice == "1":  # Coffee
    size = input("Coffee size (small/medium/large): ").strip().lower()
    item_name = "Coffee"

    if size == "medium":
        price = 4.50
        item_name += " (Medium)"
    elif size == "large":
        price = 5.50
        item_name += " (Large)"
    else:
        price = 3.50
        if size != "small":
            print("Invalid size — defaulting to Small.")
        item_name += " (Small)"
elif choice == "2":  # Sandwich
    price = 6.00
    item_name = "Sandwich"
    cheese = input("Add cheese? (yes/no): ").strip().lower()
    if cheese == "yes":
        price += 0.75
        item_name += " + Cheese"
elif choice == "3":  # Salad
    price = 5.50
    item_name = "Salad"

    dressing = input("Choose dressing (ranch/italian/vinaigrette/none): ").strip().lower()
    valid = ["ranch", "italian", "vinaigrette", "none"]

    if dressing not in valid:
        print("Invalid dressing — defaulting to none.")
        dressing = "none"

    if dressing != "none":
        item_name += f" ({dressing.title()})"
elif choice == "4":  # Combo
    price = 8.00
    item_name = "Combo"
    size = input("Coffee size (small/medium/large): ").strip().lower()
    if size == "medium":
        price += 1.00
    elif size == "large":
        price += 2.00
    elif size != "small":
        print("Invalid size — defaulting to Small.")
    cheese = input("Add cheese to sandwich? (yes/no): ").strip().lower()
    if cheese == "yes":
        price += 0.75
        item_name += " + Cheese"
elif choice == "5":
    print("Goodbye!")
    exit()
else:
    print("Invalid menu choice.")
    exit()
name = input("\nEnter your name: ").strip()
while name == "":
    print("Name cannot be empty.")
    name = input("Enter your name: ").strip()
while True:
    qty_input = input("How many? ")
    try:
        quantity = int(qty_input)
        if quantity > 0:
            break
        else:
            print("Quantity must be positive.")
    except:
        print("Please enter a valid integer.")
subtotal = price * quantity
tax = subtotal * 0.07
total = subtotal + tax
print("\n==============================")
print("         ORDER RECEIPT")
print("==============================")
print(f"Customer: {name}")
print(f"Item:     {item_name}")
print(f"Quantity: {quantity}")
print(f"Unit Price: ${price:.2f}")
print(f"Subtotal:   ${subtotal:.2f}")
print(f"Tax (7%):   ${tax:.2f}")
print(f"Total:      ${total:.2f}")
print("==============================")
print("\nThank you for your order!")
'''