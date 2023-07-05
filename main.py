class MenuItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.description} - ${self.price}"


class MenuBook:
    def __init__(self):
        self.menu = []

    def add_item(self, name, description, price):
        item = MenuItem(name, description, price)
        self.menu.append(item)

    def remove_item(self, name):
        for item in self.menu:
            if item.name.lower() == name.lower():
                self.menu.remove(item)
                return True
        return False

    def display_menu(self):
        if not self.menu:
            print("Menu is empty.")
        else:
            for item in self.menu:
                print(item)

    def get_item_by_name(self, name):
        for item in self.menu:
            if item.name.lower() == name.lower():
                return item
        return None


# Example usage:
menu_book = MenuBook()

# Adding menu items
menu_book.add_item("Burger", "A juicy beef burger", 10.99)
menu_book.add_item("Pizza", "Italian style pizza", 12.99)
menu_book.add_item("Salad", "Fresh garden salad", 8.99)
menu_book.add_item("Ice Cream", "Variety of ice cream flavors", 6.99)

# Displaying menu
menu_book.display_menu()

# Removing an item
menu_book.remove_item("Salad")

# Displaying updated menu
menu_book.display_menu()

# Getting item by name
item = menu_book.get_item_by_name("Pizza")
if item:
    print("Item found:", item)
else:
    print("Item not found.")
