class FoodItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
    def __str__(self):
        return f"{self.name} - {self.description}, Price: ${self.price}"

class Menu:
    def __init__(self):
        self.menu_items = []
    def add_item(self, item):
        self.menu_items.append(item)
        print(f"{item.name} has been added to the menu.")
    def remove_item(self, item):
        if item in self.menu_items:
            self.menu_items.remove(item)
            print(f"{item.name} has been removed from the menu.")
        else:
            print(f"{item.name} is not in the menu.")
    def display_menu(self):
        print("Menu:")
        for item in self.menu_items:
            print(item)
        print()

class Order:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
        print(f"{item.name} has been added to the order.")
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item.name} has been removed from the order.")
        else:
            print(f"{item.name} is not in the order.")
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

class Restaurant:
    def __init__(self):
        self.menu = Menu()
        self.order = Order()
    def place_order(self, item):
        self.order.add_item(item)
    def remove_order(self, item):
        self.order.remove_item(item)
    def generate_bill(self):
        total = self.order.calculate_total()
        print("Bill:")
        for item in self.order.items:
            print(item)
        print(f"Total: ${total}")
    def save_order(self, filename):
        with open(filename, "w") as file:
            file.write("Order:\n")
            for item in self.order.items:
                file.write(str(item) + "\n")

restaurant = Restaurant()

pizza = FoodItem("Pizza", "Delicious pizza with various toppings", 12.99)
burger = FoodItem("Burger", "Juicy burger with fries", 9.99)
pasta = FoodItem("Pasta", "Classic pasta with marinara sauce", 8.99)
restaurant.menu.add_item(pizza)
restaurant.menu.add_item(burger)
restaurant.menu.add_item(pasta)
restaurant.menu.display_menu()
restaurant.place_order(pizza)
restaurant.place_order(burger)
restaurant.remove_order(pizza)
restaurant.generate_bill()