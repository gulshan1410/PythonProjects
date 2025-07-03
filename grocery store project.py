
# Grocery Store Application

# Sample inventory (item: price per unit)
inventory = {
    'apple': 200,
    'banana': 80,
    'milk': 60,
    'bread': 40,
    'eggs': 15,
    'rice': 70
}

# Cart to store selected items
cart = {}

def show_inventory():
    print("\nAvailable Items:")
    for item, price in inventory.items():
        print(f"{item.capitalize()} - ₹{price}")

def add_to_cart():
    item = input("Enter item name to add: ").lower()
    if item in inventory:
        qty = int(input("Enter quantity: "))
        if item in cart:
            cart[item] += qty
        else:
            cart[item] = qty
        print(f"Added {qty} x {item} to cart.")
    else:
        print("Item not found in inventory.")

def view_cart():
    print("\nYour Cart:")
    if not cart:
        print("Cart is empty.")
        return
    total = 0
    for item, qty in cart.items():
        price = inventory[item] * qty
        total += price
        print(f"{item.capitalize()} - {qty} x ₹{inventory[item]} = ₹{price}")
    print(f"Total: ₹{total}")

def remove_from_cart():
    item = input("Enter item to remove: ").lower()
    if item in cart:
        del cart[item]
        print(f"Removed {item} from cart.")
    else:
        print("Item not found in cart.")

def checkout():
    print("\n----- Bill -----")
    view_cart()
    print("Thank you for shopping!")
    cart.clear()

def main():
    while True:
        print("\n--- Grocery Store Menu ---")
        print("1. Show Inventory")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Remove from Cart")
        print("5. Checkout")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            show_inventory()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            view_cart()
        elif choice == '4':
            remove_from_cart()
        elif choice == '5':
            checkout()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
