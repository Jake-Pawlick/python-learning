# ============================================
# PIZZA ORDER SYSTEM
# CS 1300 — Lecture 6 Lab
# ============================================

# ----- Menu Data (do not modify) -----
sizes = ["Personal (8\")", "Medium (12\")", "Large (16\")", "Party (20\")"]
size_prices = [6.99, 9.99, 12.99, 16.99]

topping_names = ["Pepperoni", "Mushrooms", "Green Peppers", "Onions",
"Sausage", "Bacon", "Extra Cheese", "Pineapple"]

topping_price = 1.50  # each topping, any size

# ----- Order Storage -----
order_descriptions = []  # e.g., "Large Pepperoni, Mushrooms"
order_prices = []        # e.g., 15.99

# Your code goes below this line.

print("Welcome to the CS 1300 Pizza Shop!\n")

# ===== ORDERING LOOP =====
while True:

    # EXERCISE 1 — Display the size menu
    print("==============================")
    print("PIZZA SIZES")
    print("==============================")
    for i in range(len(sizes)):
        print(f"{i+1}. {sizes[i]} ${size_prices[i]:>5.2f}")
    print("==============================")

    # EXERCISE 2 — Get a valid size choice
    while True:
        choice = input("Pick a size (1-4): ")
        if not choice.isdigit():
            print("Please enter a number!")
            continue

        choice = int(choice)
        if choice < 1 or choice > 4:
            print("Choose 1-4.")
            continue

        size_choice = choice - 1
        base_price = size_prices[size_choice]
        break

    # EXERCISE 3 — Add toppings
    selected_toppings = []

    print("\nAvailable toppings ($1.50 each):")
    for i in range(len(topping_names)):
        print(f"{i+1}. {topping_names[i]}")

    while True:
        t = input("Add topping # (or 'done'): ").lower()

        if t == "done":
            break

        if not t.isdigit():
            print("Enter a number or 'done'.")
            continue

        t = int(t)
        if t < 1 or t > len(topping_names):
            print("Invalid topping number.")
            continue

        topping = topping_names[t-1]

        if topping in selected_toppings:
            print(f"Already added {topping}!")
            continue

        selected_toppings.append(topping)
        print(f"✓ Added {topping}")

    # EXERCISE 4 — Calculate price and store the pizza
    total_price = base_price + (len(selected_toppings) * topping_price)

    if len(selected_toppings) == 0:
        desc = sizes[size_choice] + " Cheese"
    else:
        desc = sizes[size_choice] + " " + ", ".join(selected_toppings)

    order_descriptions.append(desc)
    order_prices.append(total_price)

    # EXERCISE 5 — Order another pizza?
    while True:
        again = input("Order another pizza? (yes/no): ").lower()

        if again in ["yes", "y"]:
            break
        elif again in ["no", "n"]:
            break
        else:
            print("Please enter yes or no.")

    if again in ["no", "n"]:
        break

# ===== POST-ORDER =====
if not order_descriptions:
    print("\nNo pizzas ordered. See you next time!")
else:

    # EXERCISE 8 — Discount code
    discount = 0
    attempts = 0

    while attempts < 3:
        code = input("\nEnter discount code (or 'none'): ").upper()

        if code == "NONE":
            break
        elif code == "STUDENT10":
            discount = 0.10
            print("10% discount applied!")
            break
        elif code == "HALFOFF":
            discount = 0.50
            print("50% discount applied!")
            break
        else:
            attempts += 1
            print("Invalid code.")

    if attempts == 3:
        print("No discount applied.")

    # EXERCISE 6 — Print receipt
    print("\n====================================")
    print("YOUR ORDER RECEIPT")
    print("====================================")

    subtotal = 0

    for i in range(len(order_descriptions)):
        print(f"{i+1}. {order_descriptions[i]}")
        print(f"${order_prices[i]:>6.2f}")
        subtotal += order_prices[i]

    if discount > 0:
        subtotal = subtotal - (subtotal * discount)

    tax = subtotal * 0.07
    total = subtotal + tax

    print("------------------------------------")
    print(f"Subtotal: ${subtotal:>6.2f}")
    print(f"Tax (7%): ${tax:>6.2f}")
    print(f"Total:    ${total:>6.2f}")
    print("====================================")

    # EXERCISE 7 — Find most expensive pizza
    max_price = order_prices[0]
    max_index = 0

    for i in range(len(order_prices)):
        if order_prices[i] > max_price:
            max_price = order_prices[i]
            max_index = i

    print(f"\nMost expensive pizza: {order_descriptions[max_index]} (${max_price:.2f})")

    # EXERCISE 9 — Count pizzas by size
    counts = [0, 0, 0, 0]

    for desc in order_descriptions:
        for i in range(len(sizes)):
            if sizes[i] in desc:
                counts[i] += 1

    print("\nPizza count by size:")
    for i in range(len(sizes)):
        print(f"{sizes[i]}: {counts[i]}")

print("\nThank you for your order!")