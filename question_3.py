#question 3 task 1
def process_order(orders):
    for order in orders:
        customer_name, product, quantity = order
        print(f"Customer: {customer_name}, Product: {product}, Quantity: {quantity}")

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Smartphone", 3),
    ("Diana", "Headphones", 5),
]

process_order(orders)