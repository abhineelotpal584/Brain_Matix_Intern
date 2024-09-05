class ATM:
    def __init__(self, balance=0):
        """Initialize the ATM with an optional starting balance and a default PIN."""
        self.balance = balance
        self.pin = 1234  # Default PIN (can be customized)

    def check_pin(self):
        """Check if the entered PIN is correct. Allows 3 attempts."""
        tries = 3  # User has 3 attempts to enter the correct PIN
        while tries > 0:
            entered_pin = int(input("Enter your PIN: "))
            if entered_pin == self.pin:  # Check if the entered PIN matches the stored PIN
                print("PIN accepted.")
                return True
            else:
                tries -= 1  # Decrement the number of remaining tries
                print(f"Incorrect PIN. You have {tries} attempt(s) left.")
        
        # If all attempts are used, lock the user out
        print("Too many incorrect attempts. Exiting...")
        return False

    def check_balance(self):
        """Display the user's current balance."""
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        """Deposit the given amount into the user's account."""
        if amount > 0:
            self.balance += amount  # Add the deposited amount to the balance
            print(f"Successfully deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount.")  # Reject negative or zero deposits

    def withdraw(self, amount):
        """Withdraw the given amount from the user's account if sufficient balance is available."""
        if 0 < amount <= self.balance:  # Check if the amount is valid and available
            self.balance -= amount  # Deduct the withdrawn amount from the balance
            print(f"Successfully withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds or invalid amount.")  # Handle invalid withdrawals

    def change_pin(self):
        """Allow the user to change their PIN after entering the current PIN correctly."""
        old_pin = int(input("Enter your current PIN: "))  # Ask for the current PIN
        if old_pin == self.pin:  # Validate the current PIN
            new_pin = int(input("Enter your new PIN: "))
            confirm_pin = int(input("Confirm your new PIN: "))
            if new_pin == confirm_pin:  # Ensure that the new PIN matches the confirmation
                self.pin = new_pin  # Update the PIN
                print("PIN changed successfully.")
            else:
                print("PINs do not match. Try again.")
        else:
            print("Incorrect PIN. Cannot change PIN.")

    def start(self):
        """Start the ATM interface if the user enters the correct PIN."""
        if self.check_pin():  # Only proceed if the correct PIN is entered
            while True:
                # Display the menu options to the user
                print("\nATM Menu:")
                print("1. Check Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Change PIN")
                print("5. Exit")
                
                choice = int(input("Choose an option: "))  # Get the user's choice

                # Execute the corresponding function based on the user's choice
                if choice == 1:
                    self.check_balance()  # Check balance
                elif choice == 2:
                    amount = float(input("Enter deposit amount: "))
                    self.deposit(amount)  # Deposit money
                elif choice == 3:
                    amount = float(input("Enter withdrawal amount: "))
                    self.withdraw(amount)  # Withdraw money
                elif choice == 4:
                    self.change_pin()  # Change PIN
                elif choice == 5:
                    print("Thank you for using the ATM. Goodbye!")
                    break  # Exit the ATM interface
                else:
                    print("Invalid option. Please try again.")  # Handle invalid menu choices


# Example usage of the ATM system:
atm = ATM(balance=1000)  # Initialize ATM with a starting balance of $1000
atm.start()  # Start the ATM interface

