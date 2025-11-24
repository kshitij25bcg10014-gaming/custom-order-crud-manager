import json
import os

DATA_FILE = "orders.json"

def load_orders():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_orders(orders):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(orders, f, indent=4)

def create_order():
    orders = load_orders()
    order_id = len(orders) + 1
    customer_name = input("Enter customer name: ").strip()
    product = input("Enter product: ").strip()
    quantity = input("Enter quantity: ").strip()
    try:
        quantity = int(quantity)
    except ValueError:
        print("Invalid quantity, needs to be a number.")
        return
    
    order = {
        "order_id": order_id,
        "customer_name": customer_name,
        "product": product,
        "quantity": quantity
    }
    orders.append(order)
    save_orders(orders)
    print(f"Order created with ID {order_id}.")

def list_orders():
    orders = load_orders()
    if not orders:
        print("No orders found.")
        return
    print("\nCustomer Orders:")
    for o in orders:
        print(f"ID: {o['order_id']} | Customer: {o['customer_name']} | Product: {o['product']} | Quantity: {o['quantity']}")
    print()

def update_order():
    orders = load_orders()
    if not orders:
        print("No orders found.")
        return
    try:
        order_id = int(input("Enter order ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return
    for order in orders:
        if order["order_id"] == order_id:
            print(f"Current info: Customer: {order['customer_name']}, Product: {order['product']}, Quantity: {order['quantity']}")
            customer_name = input("Enter new customer name (leave blank to keep): ").strip()
            product = input("Enter new product (leave blank to keep): ").strip()
            quantity = input("Enter new quantity (leave blank to keep): ").strip()
            if customer_name:
                order["customer_name"] = customer_name
            if product:
                order["product"] = product
            if quantity:
                try:
                    order["quantity"] = int(quantity)
                except ValueError:
                    print("Invalid quantity entered. Update aborted.")
                    return
            save_orders(orders)
            print("Order updated.")
            return
    print("Order ID not found.")

def delete_order():
    orders = load_orders()
    if not orders:
        print("No orders found.")
        return
    try:
        order_id = int(input("Enter order ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return
    for i, order in enumerate(orders):
        if order["order_id"] == order_id:
            del orders[i]
            # Re-assign IDs to keep consistent
            for idx, o in enumerate(orders, start=1):
                o["order_id"] = idx
            save_orders(orders)
            print("Order deleted.")
            return
    print("Order ID not found.")

def main_menu():
    while True:
        print("=== Customer Order CRUD Manager ===")
        print("1. Create order")
        print("2. List orders")
        print("3. Update order")
        print("4. Delete order")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            create_order()
        elif choice == "2":
            list_orders()
        elif choice == "3":
            update_order()
        elif choice == "4":
            delete_order()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main_menu()
