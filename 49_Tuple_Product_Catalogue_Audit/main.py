products = [
    (101, "Notebook", 40.0, 12),
    (102, "Pen", 10.0, 3),
    (103, "Bag", 650.0, 2)
]

total_value = 0

for product in products:
    product_id, name, price, quantity = product
    value = price * quantity
    total_value += value
    print(f"{product_id} {name}: Stock value = Rs. {value:.2f}")

    if quantity < 5:
        print("  Replenishment required")

print(f"Total inventory value: Rs. {total_value:.2f}")
