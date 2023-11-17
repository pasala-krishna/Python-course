class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
        print(f"Added {quantity} {item}(s) to the cart.")

    def remove_item(self, item, quantity=1):
        if item in self.items:
            if self.items[item] > quantity:
                self.items[item] -= quantity
                print(f"Removed {quantity} {item}(s) from the cart.")
            else:
                del self.items[item]
                print(f"Removed all {item}(s) from the cart.")
        else:
            print(f"{item} not found in the cart.")

    def calculate_total(self, prices):
        total_cost = 0
        for item, quantity in self.items.items():
            if item in prices:
                total_cost += prices[item] * quantity
        return total_cost

    def display_cart(self):
        if not self.items:
            print("The cart is empty.")
        else:
            print("Items in the cart:")
            for item, quantity in self.items.items():
                print(f"{item}: {quantity}")

# Example usage:
prices = {
    "apple": 0.5,
    "banana": 0.3,
    "orange": 0.6,
}

cart = ShoppingCart()

cart.add_item("apple", prices["apple"], 3)
cart.add_item("banana", prices["banana"], 2)
cart.display_cart()

total_cost = cart.calculate_total(prices)
print(f"Total cost: ${total_cost:.2f}")

cart.remove_item("apple", 2)
cart.display_cart()

total_cost = cart.calculate_total(prices)
print(f"Updated total cost: ${total_cost:.2f}")
