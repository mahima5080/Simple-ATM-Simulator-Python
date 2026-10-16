# Simple ATM Simulator - Week 1 Assignment

# Global Variables
DEFAULT_PIN = "1234"
balance = 1000.0  # Starting balance


def check_balance(current_balance):
    """Function to display current account balance."""
    print(f"\n[ACCOUNT BALANCE]: ${current_balance:,.2f}")


def deposit(current_balance):
    """Function to handle money deposit."""
    try:
        amount = float(input("Enter amount to deposit: $"))
        if amount > 0:
            current_balance += amount
            print(f"Successfully deposited ${amount:,.2f}!")
            print(f"Updated Balance: ${current_balance:,.2f}")
        else:
            print("Error: Deposit amount must be greater than $0.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid numerical amount.")
    return current_balance


def withdraw(current_balance):
    """Function to handle money withdrawal."""
    try:
        amount = float(input("Enter amount to withdraw: $"))
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than $0.")
        elif amount > current_balance:
            print("Error: Insufficient funds!")
            print(f"Your available balance is ${current_balance:,.2f}.")
        else:
            current_balance -= amount
            print(f"Successfully withdrew ${amount:,.2f}!")
            print(f"Remaining Balance: ${current_balance:,.2f}")
    except ValueError:
        print("Error: Invalid input. Please enter a valid numerical amount.")
    return current_balance


def authenticate_user():
    """Function to handle PIN-based user login with a maximum of 3 attempts."""
    attempts = 3
    print("==========================================")
    print("         WELCOME TO THE PYTHON ATM        ")
    print("==========================================")

    while attempts > 0:
        entered_pin = input("\nPlease enter your 4-digit PIN: ")
        if entered_pin == DEFAULT_PIN:
            print("Authentication successful! Access granted.\n")
            return True
        else:
            attempts -= 1
            print(f"Incorrect PIN. Attempts remaining: {attempts}")

    print("\nAccount locked due to too many failed attempts.")
    return False


def main():
    global balance

    # Step 1: User Login
    if not authenticate_user():
        return

    # Step 2: ATM Menu Loop
    while True:
        print("\n------------------------------------------")
        print("               ATM MENU                   ")
        print("------------------------------------------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("\nThank you for using the Python ATM. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a valid option between 1 and 4.")


# Run the ATM Simulator
if __name__ == "__main__":
    main()