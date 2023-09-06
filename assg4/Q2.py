class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.table_reservations = []
        self.customer_orders = []

    def add_item_to_menu(self, item_name, item_price):
        """Add an item to the restaurant's menu."""
        self.menu_items[item_name] = item_price

    def book_table(self, table_number):
        """Book a table for a reservation."""
        if table_number not in self.table_reservations:
            self.table_reservations.append(table_number)
            print(f"Table {table_number} has been booked.")
        else:
            print(f"Table {table_number} is already booked. Please choose another table.")

    def customer_order(self, table_number, item_name):
        """Take a customer's order for a specific table."""
        if table_number in self.table_reservations:
            if item_name in self.menu_items:
                self.customer_orders.append((table_number, item_name))
                print(f"Order for table {table_number}: {item_name}")
            else:
                print(f"{item_name} is not on the menu.")
        else:
            print(f"Table {table_number} is not reserved. Please book a table first.")

    def print_menu(self):
        """Print the restaurant's menu."""
        print("Menu:")
        for item_name, item_price in self.menu_items.items():
            print(f"{item_name}: Rs {item_price}")

    def print_reservations(self):
        """Print the table reservations."""
        print("Table Reservations:")
        for table_number in self.table_reservations:
            print(f"Table {table_number}")

    def print_customer_orders(self):
        """Print the customer orders."""
        print("Customer Orders:")
        for table_number, item_name in self.customer_orders:
            print(f"Table {table_number}: {item_name}")

restaurant = Restaurant()

restaurant.add_item_to_menu("Burger", 100)
restaurant.add_item_to_menu("Pizza", 200)
restaurant.add_item_to_menu("Pasta", 250)

restaurant.book_table(1)
restaurant.book_table(2)
restaurant.book_table(1)

restaurant.customer_order(1, "Burger")
restaurant.customer_order(2, "Pizza")
restaurant.customer_order(3, "Burger")
restaurant.customer_order(1, "Salad")

restaurant.print_menu()
restaurant.print_reservations()
restaurant.print_customer_orders()