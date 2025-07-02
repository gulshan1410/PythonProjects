# ATM Project using Exception Handling

# Initial balance (You can also load from a file)
balance = 10000
pin_code = "1234"

def check_pin():
    try:
        pin = input("Enter your 4-digit PIN: ")
        if pin != pin_code:
            raise ValueError("Incorrect PIN")
        return True
    except ValueError as e:
        print("Error:", e)
        return False

def check_balance():
    print(f"Your current balance is: ₹{balance}")

def deposit():
    global balance
    try:
        amount = float(input("Enter amount to deposit: ₹"))
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        balance += amount
        print(f"₹{amount} deposited successfully.")
    except ValueError as e:
        print("Error:", e)

def withdraw():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > balance:
            raise ValueError("Insufficient funds.")
        balance -= amount
        print(f"₹{amount} withdrawn successfully.")
    except ValueError as e:
        print("Error:", e)

def atm_menu():
    while True:
        print("\n------ ATM Menu ------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Select your option (1-4): ")

        try:
            if choice == '1':
                check_balance()
            elif choice == '2':
                deposit()
            elif choice == '3':
                withdraw()
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                raise ValueError("Invalid option. Please choose from 1 to 4.")
        except ValueError as e:
            print("Error:", e)

# Main program
print("Welcome to the ATM!")
if check_pin():
    atm_menu()
else:
    print("Access denied due to incorrect PIN.")
