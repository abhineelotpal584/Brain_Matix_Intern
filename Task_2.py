# Class to represent a single inventory item
class InventoryItem:
    def __init__(self, name, quantity, price):
        """
        Initialize an inventory item with name, quantity, and price.
        
        :param name: Name of the item
        :param quantity: Quantity of the item
        :param price: Price per unit of the item
        """
        self.name = name       # Name of the item
        self.quantity = quantity  # Number of units of the item
        self.price = price     # Price of each unit of the item

    def __str__(self):
        """
        String representation of the inventory item, 
        showing its name, quantity, and price.
        """
        return f"Item: {self.name}, Quantity: {self.quantity}, Price: {self.price}"

# Class to manage the entire inventory
class InventoryManagement:
    def __init__(self):
        """
        Initialize the inventory management system. 
        It uses a dictionary to store inventory items where the item name is the key.
        """
        self.inventory = {}

    def add_item(self, name, quantity, price):
        """
        Add an item to the inventory. If the item already exists, update its quantity.
        
        :param name: Name of the item to add
        :param quantity: Quantity to add
        :param price: Price per unit
        """
        # Check if item already exists in inventory
        if name in self.inventory:
            # If it exists, increase the quantity
            self.inventory[name].quantity += quantity
        else:
            # If it does not exist, create a new InventoryItem and add it
            self.inventory[name] = InventoryItem(name, quantity, price)
        print(f"Added {quantity} {name}(s) to inventory.")

    def update_stock(self, name, quantity):
        """
        Update the stock (quantity) of an item in the inventory.
        
        :param name: Name of the item to update
        :param quantity: New quantity to set
        """
        if name in self.inventory:
            # If the item exists, update its quantity
            self.inventory[name].quantity = quantity
            print(f"Updated stock for {name}. New quantity: {quantity}")
        else:
            # If the item does not exist, display an error message
            print(f"Item {name} not found in inventory.")

    def remove_item(self, name):
        """
        Remove an item from the inventory.
        
        :param name: Name of the item to remove
        """
        if name in self.inventory:
            # Remove the item from the inventory dictionary
            del self.inventory[name]
            print(f"Removed {name} from inventory.")
        else:
            # If the item does not exist, display an error message
            print(f"Item {name} not found in inventory.")

    def view_inventory(self):
        """
        View all items currently in the inventory.
        """
        if not self.inventory:
            # If the inventory is empty, display a message
            print("Inventory is empty.")
        else:
            # Iterate through all items in the inventory and print them
            for item in self.inventory.values():
                print(item)

    def check_stock(self, name):
        """
        Check the stock (quantity) of a specific item in the inventory.
        
        :param name: Name of the item to check
        """
        if name in self.inventory:
            # If the item exists, print its quantity
            print(f"{name}: {self.inventory[name].quantity} in stock.")
        else:
            # If the item does not exist, display an error message
            print(f"{name} not found in inventory.")

# Function to display a menu for interacting with the inventory management system
def menu():
    """
    Displays a menu for interacting with the inventory system. 
    The user can add, update, remove, or view items, as well as exit the program.
    """
    inventory = InventoryManagement()  # Create an instance of the inventory management system

    while True:
        # Display the menu options
        print("\n1. Add Item")
        print("2. Update Stock")
        print("3. Remove Item")
        print("4. View Inventory")
        print("5. Check Stock")
        print("6. Exit")

        # Get the user's choice
        choice = input("Enter your choice: ")

        # Add a new item to the inventory
        if choice == "1":
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            inventory.add_item(name, quantity, price)

        # Update the stock for an existing item
        elif choice == "2":
            name = input("Enter item name: ")
            quantity = int(input("Enter new quantity: "))
            inventory.update_stock(name, quantity)

        # Remove an item from the inventory
        elif choice == "3":
            name = input("Enter item name: ")
            inventory.remove_item(name)

        # View all items in the inventory
        elif choice == "4":
            inventory.view_inventory()

        # Check the stock of a specific item
        elif choice == "5":
            name = input("Enter item name: ")
            inventory.check_stock(name)

        # Exit the program
        elif choice == "6":
            print("Exiting...")
            break

        # Handle invalid input
        else:
            print("Invalid choice. Please try again.")

# Main entry point for the program
if __name__ == "__main__":
    menu()
