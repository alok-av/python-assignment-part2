import copy

def task_1():
    print("=== Task 1: Explore the Menu ===\n")
    menu = {
        "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
        "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
        "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
        "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
        "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
        "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
        "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
        "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
        "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
        "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
    }

    categories = []
    for details in menu.values():
        if details["category"] not in categories:
            categories.append(details["category"])

    for cat in categories:
        print(f"===== {cat} =====")
        for item_name, details in menu.items():
            if details["category"] == cat:
                avail_str = "[Available]" if details["available"] else "[Unavailable]"
                print(f"{item_name:<16} ₹{details['price']:<7.2f} {avail_str}")
        print()

    total_items = len(menu)
    available_items = sum(1 for v in menu.values() if v["available"])

    max_price = 0
    most_expensive_item = ""
    for item, details in menu.items():
        price = float(details["price"])  # type: ignore
        if price > max_price:
            max_price = price
            most_expensive_item = item

    items_under_150 = [(item, details["price"]) for item, details in menu.items() if float(details["price"]) < 150]  # type: ignore

    print(f"Total number of items on the menu: {total_items}")
    print(f"Total number of available items: {available_items}")
    print(f"Most expensive item: {most_expensive_item} (₹{max_price:.2f})")
    print("Items priced under ₹150:")
    for item, price in items_under_150:
        print(f"  - {item} (₹{price:.2f})")
    print("\n" + "="*50 + "\n")
    return menu


def task_2(menu):
    print("=== Task 2: Cart Operations ===\n")
    cart = []

    def add_to_cart(item_name, quantity=1):
        if item_name not in menu:
            print(f"Cannot add '{item_name}': Item does not exist in menu.")
            return
        if not menu[item_name]["available"]:
            print(f"Cannot add '{item_name}': Item is currently unavailable.")
            return
        
        # Check if already in cart
        for entry in cart:
            if entry["item"] == item_name:
                entry["quantity"] += quantity
                print(f"Updated '{item_name}' quantity to {entry['quantity']}.")
                return
                
        # If not in cart, add it
        cart.append({"item": item_name, "quantity": quantity, "price": menu[item_name]["price"]})
        print(f"Added {quantity} x '{item_name}' to cart.")

    def remove_from_cart(item_name):
        for entry in cart:
            if entry["item"] == item_name:
                cart.remove(entry)
                print(f"Removed '{item_name}' from cart.")
                return
        print(f"Cannot remove '{item_name}': Item is not in cart.")

    def print_cart():
        print("Current Cart:", cart)

    # Sequence Operations
    add_to_cart("Paneer Tikka", 2)
    print_cart()

    add_to_cart("Gulab Jamun", 1)
    print_cart()

    add_to_cart("Paneer Tikka", 1)
    print_cart()

    add_to_cart("Mystery Burger", 1)
    print_cart()

    add_to_cart("Chicken Wings", 1)
    print_cart()

    remove_from_cart("Gulab Jamun")
    print_cart()

    print("\n========== Order Summary ==========")
    subtotal = 0
    for entry in cart:
        item_total = entry["quantity"] * entry["price"]
        subtotal += item_total
        print(f"{entry['item']:<18} x{entry['quantity']:<4} ₹{item_total:.2f}")

    print("-" * 36)
    gst = subtotal * 0.05
    total_payable = subtotal + gst
    print(f"Subtotal:                ₹{subtotal:6.2f}")
    print(f"GST (5%):                ₹{gst:6.2f}")
    print(f"Total Payable:           ₹{total_payable:6.2f}")
    print("====================================")
    print("\n" + "="*50 + "\n")
    return cart


def task_3(cart):
    print("=== Task 3: Inventory Tracker with Deep Copy ===\n")
    inventory = {
        "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
        "Chicken Wings":  {"stock":  8, "reorder_level": 2},
        "Veg Soup":       {"stock": 15, "reorder_level": 5},
        "Butter Chicken": {"stock": 12, "reorder_level": 4},
        "Dal Tadka":      {"stock": 20, "reorder_level": 5},
        "Veg Biryani":    {"stock":  6, "reorder_level": 3},
        "Garlic Naan":    {"stock": 30, "reorder_level": 10},
        "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
        "Rasgulla":       {"stock":  4, "reorder_level": 3},
        "Ice Cream":      {"stock":  7, "reorder_level": 4},
    }

    inventory_backup = copy.deepcopy(inventory)

    # Modify original to prove deep copy
    inventory["Paneer Tikka"]["stock"] = 999
    print("--- Proving Deep Copy ---")
    print(f"original modified    -> inventory['Paneer Tikka']['stock'] = {inventory['Paneer Tikka']['stock']}")
    print(f"backup unmodified    -> inventory_backup['Paneer Tikka']['stock'] = {inventory_backup['Paneer Tikka']['stock']}")
    print()

    # Restore original from backup
    inventory = copy.deepcopy(inventory_backup)

    # Simulate order fulfillment using final cart
    print("--- Order Fulfillment ---")
    for entry in cart:
        item_name = entry["item"]
        qty_needed = entry["quantity"]
        
        current_stock = inventory[item_name]["stock"]
        if current_stock >= qty_needed:
            inventory[item_name]["stock"] -= qty_needed
            print(f"Fulfilled {qty_needed} x {item_name} (Remaining stock: {inventory[item_name]['stock']})")
        else:
            print(f"Warning: Insufficient stock for {item_name}. Fulfilling only exactly {current_stock} available units.")
            inventory[item_name]["stock"] = 0

    print("\n--- Reorder Alerts ---")
    for item, details in inventory.items():
        if details["stock"] <= details["reorder_level"]:
            print(f"⚠ Reorder Alert: {item} — Only {details['stock']} unit(s) left (reorder level: {details['reorder_level']})")

    print("\n--- Final Check: Deep Copy Integrity ---")
    print(f"inventory['Paneer Tikka']['stock'] = {inventory['Paneer Tikka']['stock']}")
    print(f"inventory_backup['Paneer Tikka']['stock'] = {inventory_backup['Paneer Tikka']['stock']}")
    print("\n" + "="*50 + "\n")


def task_4():
    print("=== Task 4: Daily Sales Log Analysis ===\n")
    sales_log = {
        "2025-01-01": [
            {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
            {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
            {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
        ],
        "2025-01-02": [
            {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
            {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
        ],
        "2025-01-03": [
            {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
            {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
            {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
        ],
        "2025-01-04": [
            {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
            {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
        ],
    }

    # Helper to print revenue
    def print_revenue_stats(log_dict):
        best_day = None
        max_rev = 0
        print("Revenue per Day:")
        for date, orders_list in log_dict.items():
            day_total = sum(order["total"] for order in orders_list)
            print(f"  {date}: ₹{day_total:.2f}")
            if day_total > max_rev:
                max_rev = day_total
                best_day = date
        print(f"\nBest-selling day: {best_day} (₹{max_rev:.2f})\n")

    print_revenue_stats(sales_log)

    # Find most ordered item (appears in most distinct orders)
    item_order_counts: dict[str, int] = {}
    for date, orders_list in sales_log.items():
        for order in orders_list:
            items = order.get("items", [])
            if isinstance(items, list):
                for item in items:
                    # The question asks "appears in the greatest number of individual orders"
                    item_order_counts[item] = item_order_counts.get(item, 0) + 1

    most_ordered_item = max(item_order_counts, key=item_order_counts.get)  # type: ignore
    print(f"Most ordered item (appears in {item_order_counts[most_ordered_item]} unique orders): {most_ordered_item}\n")

    # Add new day
    print("--- Adding new day (2025-01-05) ---")
    sales_log["2025-01-05"] = [
        {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
        {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
    ]
    print_revenue_stats(sales_log)

    # Numbered list of all orders
    print("--- All Orders ---")
    all_orders = []
    for date, orders_list in sales_log.items():
        for order in orders_list:
            all_orders.append((date, order))

    for idx, (date, order) in enumerate(all_orders, 1):
        items_str = ", ".join(order["items"])
        print(f"{idx}.  [{date}] Order #{order['order_id']}  — ₹{order['total']:.2f} — Items: {items_str}")


if __name__ == '__main__':
    menu = task_1()
    cart = task_2(menu)
    task_3(cart)
    task_4()
