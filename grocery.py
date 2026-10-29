
print("=== Grocery Billing Queue ===\n")

# ---------- PART 1: The five counters ----------
low_price_items = 0
medium_price_items = 0
high_price_items = 0

customers_served = 0
total_sales = 0

billing = True


# ---------- PART 2: The OUTER while loop ----------
while billing:
    customer_name = input("Enter customer name: ")
    item_count = int(input("How many items are they buying? "))


    # ---------- PART 3: Continue on a bad item count ----------
    if item_count <= 0:
        print("Invalid item count! Please enter a number greater than 0.\n")
        continue


    # ---------- PART 4: The INNER while loop ----------
    customer_total = 0
    item_number = 1

    while item_number <= item_count:
        item_name = input("Enter item name: ")
        price = int(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))


        # ---------- PART 5: Item total and price band ----------
        if price <= 0 or quantity <= 0:
            print("Invalid price or quantity! Please try again.")
            continue

        item_total = price * quantity

        print(f"{item_name}: {quantity} x {price} = {item_total}")

        customer_total += item_total

        # Classify items by price
        if price < 50:
            low_price_items += quantity
        elif price <= 100:
            medium_price_items += quantity
        else:
            high_price_items += quantity

        item_number += 1


    # ---------- PART 6: Finish the customer ----------
    customers_served += 1
    total_sales += customer_total

    print(f"\n{customer_name}'s total bill: {customer_total}")

    next_customer = input("Next customer? (yes/no): ").lower()

    if next_customer != "yes":
        billing = False

    print()


# ---------- PART 7: The NESTED for report ----------
print("=== Daily Sales Report ===")

price_bands = [
    ("Low-price items (< 50)", low_price_items),
    ("Medium-price items (50-100)", medium_price_items),
    ("High-price items (> 100)", high_price_items)
]

for band_name, count in price_bands:
    print(f"{band_name}: ", end="")

    for i in range(count):
        print("*", end="")

    print()

print(f"\nCustomers served: {customers_served}")
print(f"Total sales: {total_sales}")
