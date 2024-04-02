items = {
    'apple': {'quantity': 10, 'price': 5},
    'banana': {'quantity': 15, 'price': 3},
    'orange': {'quantity': 20, 'price': 4},
}


def display_menu():
    print("Available Items:")
    for item, details in items.items():
        print(f"{item.capitalize()}: {details['quantity']} available - Rs.{details['price']} each")


def accept_customer_inputs():
    cart = {}
    while True:
        item = input("Enter the item you want to purchase (or type 'done' to finish): ").lower()
        if item == 'done':
            break
        if item in items:
            quantity = int(input(f"Enter the quantity of {item}: "))
            if quantity <= items[item]['quantity']:
                cart[item] = quantity
                items[item]['quantity'] -= quantity
            else:
                print(f"Sorry, only {items[item]['quantity']} {item}(s) available.")
        else:
            print("Sorry, that item is not available.")
    return cart


def get_customer_details():
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    contact = input("Enter your contact number: ")
    return {'name': name, 'address': address, 'contact': contact}


def calculate_delivery_charges(distance):
    if distance <= 15:
        return 50
    elif 15 < distance <= 30:
        return 100
    else:
        return 0  # No delivery beyond 30 km


def display_final_bill(cart, customer_details, distance):
    print("\n*********** Final Bill ***********")
    print("Items Purchased:")
    for item, quantity in cart.items():
        print(f"{item.capitalize()}: {quantity} - Rs.{quantity * items[item]['price']}")
    delivery_charges = calculate_delivery_charges(distance)
    print(f"Delivery Charges: Rs.{delivery_charges}")
    print("Customer Details:")
    for key, value in customer_details.items():
        print(f"{key.capitalize()}: {value}")
    total_amount = sum(cart[item] * items[item]['price'] for item in cart) + delivery_charges
    print(f"Total Amount: Rs.{total_amount}")

def main():
    print("Welcome to Hackathon Shopping Cart Program!\n")
    display_menu()
    print("\nPlease enter your order:")
    cart = accept_customer_inputs()
    customer_details = get_customer_details()
    distance = float(input("Enter the distance from the store (in kilometers): "))
    display_final_bill(cart, customer_details, distance)

if __name__ == "__main__":
    main()