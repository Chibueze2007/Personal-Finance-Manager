from transaction import Transaction
from FinanceManager import FinanceManager
from storage import save_data
from datetime import datetime

# Create the FinanceManager object
manager = FinanceManager()


# Function for adding a new transaction

def add_transaction(manager):

    # Ask the user for the transaction amount
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <=0:
                print("Amount should be greater than 0.")
                continue
            
            break
        except ValueError:
            # Handle invalid input that cannot be converted to a number
            print("Invalid input. Please enter a valid number.")

    print(f"The amount entered is {amount:,}")

    # Ask the user for the transaction type
    while True:
        transaction_type = input("Enter the transaction type (credit/debit): ").lower()

        # Check that the transaction type is either credit or debit
        if transaction_type in ("credit", "debit"):
            print(f"Transaction Type: {transaction_type}")
            break
        else:
            print("Invalid transaction type. Please enter credit or debit")

    # Ask the user for the transaction category
    while True:
        category = input("Enter the category for the transaction: ").strip()

        # Make sure the category is not empty
        if category == "":
            print("Invalid category fill in the field before proceeding")
            continue
        else:
            break

    print(f"Category: {category}")

    # Ask the user for a description
    while True:
        description = input("Enter the description of the transaction: ").strip()

        # Make sure the description is not empty
        if description == "":
            print("Invalid description fill in the field before proceeding")
            continue
        else:
            break

    print(f"Description: {description}")

    # Ask the user for the transaction date
    while True:
        date = input("Enter the date: ")

        try:
            # Check that the date follows the YYYY-MM-DD format
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Enter a valid date")

    print(f"Date: {date}")

    # Create a Transaction object using the information entered by the user
    transaction = Transaction(
        amount,
        transaction_type,
        category,
        description,
        date
    )

    # Add the new transaction to the FinanceManager
    manager.add_transaction(transaction)

    # Save all transactions to the JSON file
    save_data(manager.get_data())
    print("\nTransaction added successfully!")
# Function for viewing transaction

def view_transactions(manager):
    print("\n========ALL TRANSACTIONS=====")
    manager.view_transactions()

# Function for viewing total income
def view_income(manager):
    print("\n========TOTAL INCOME=====")
    income = manager.calc_total_income()
    print(f"Total Income: ₦{income:,}")

# Function for viewing total expenses
def view_expenses(manager):
    print("\n========TOTAL EXPENSES=====")
    expense = manager.calc_total_expenses()
    print(f"Total Expenses: ₦{expense:,}")

# Function for viewing current balance
def view_balance(manager):
    print("\n========CURRENT BALANCE=====")
    balance = manager.calc_balance()
    print(f"Current Balance: ₦{balance:,}")

# Function for searching transactions by description
def search_transactions(manager):
    print("\n========SEARCH TRANSACTIONS=====")
    while True:
        search_term = input("Enter a description that you want to search for: ").strip()

        if search_term:
            manager.search_by_description(search_term)
            break
        else:
            print("Search term cannot be empty. Please enter a valid description.")

# Function for filtering transactions by category or type
def filter_transactions(manager):
    print("\n========FILTER TRANSACTIONS=====")
    filter_type = input("Filter by category or type: ").strip().lower()
    if filter_type == "category":
        while True:
            category = input("Enter the category to filter by: ").strip()
            if category:
                manager.filter_by_category(category)
                break
            else:
                print("Category cannot be empty. Please enter a valid category.")
    elif filter_type == "type":
        while True:
            transaction_type = input("Enter the transaction type to filter by (credit/debit): ").strip().lower()

            if transaction_type in ("credit", "debit"):
                manager.filter_by_type(transaction_type)
                break
            else:
                print("Invalid transaction type. Please enter 'credit' or 'debit'.")
    else:
        print("Invalid filter type. Please enter 'category' or 'type'.")            
    
def edit_transactions(manager):
    while True:
        try:
            transaction_id = int(input("Enter the transaction ID you want to edit: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid transaction ID.")
    transaction = manager.find_transaction_by_id(transaction_id)
    if transaction is None:
        print("Transaction not found")
        return
    print("\nWhat do you want to edit? ")
    print("1. Amount")
    print("2. Transaction Type")
    print("3. Category")
    print("4. Description")
    print("5. Date")
    choice = input("Enter your choice(1-5): ")
    while choice not in ("1", "2", "3", "4", "5"):
        choice = input("Invalid choice. Please enter a number from 1 to 5: ")
    if choice == "1":
        field = "amount"
    elif choice == "2":
        field = "transaction_type"
    elif choice == "3":
        field = "category"
    elif choice == "4":
        field = "description"
    elif choice == "5":
        field = "date"
   
    new_value = input("Enter the new value: ")
    while True:
        try:
            if field =="amount":
                new_value = float(new_value)
                
                if new_value <= 0:
                    raise ValueError("Amount should be greater than 0")
            elif field == "transaction_type":
                    if new_value.lower() not in ("credit", "debit"):
                        raise ValueError("Transaction type should be either credit or debit")
            elif field == "category":
                    if not new_value.strip():
                        raise ValueError("Category cannot be empty")
            elif field == "description":
                    if not new_value.strip():
                        raise ValueError("Description cannot be empty") 
            elif field == "date":
                    try:
                        datetime.strptime(new_value, "%Y-%m-%d")
                    except ValueError:
                        raise ValueError("Incorrect date format. Please use YYYY-MM-DD.")
            break
        except ValueError as error:
            print(f"Invalid input: {error}")
            new_value = input("Enter the new value: ")
    success = manager.edit_transactions(transaction_id,field,new_value)
    if success:
        print("Transaction updated successfully")
# Display the main menu and get the user's choice
def show_menu():
    print("\n========PERSONAL FINANCE MANAGER=====")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. View Total Income")
    print("4. View Total Expenses")
    print("5. View Current Balance")
    print("6. Search Transactions by Description")
    print("7. Filter Transactions by Category or Transaction Type")
    print("8. Edit Transactions")
    print("9. Delete Transaction")
    print("10. View Financial Summary")
    print("11. Exit")
    while True:
        choice = input("Enter your choice (1-11): ")
        if choice in("1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11"):
            return choice
        else:
            
            print("Invalid choice. Please enter a number from 1 to 11.")

# Run the main program menu until the user chooses to exit
def run_menu(manager):
    while True:
        choice = show_menu()
        if choice == "1":
            add_transaction(manager)
        elif choice == "2":
            view_transactions(manager)
        elif choice == "3":
            view_income(manager)
        elif choice == "4":
            view_expenses(manager)
        elif choice == "5":
            view_balance(manager)
        elif choice == "6":
            search_transactions(manager)
        elif choice == "7":
            filter_transactions(manager)
        elif choice == "8":
            edit_transactions(manager)
        elif choice == "9":
            delete_transaction(manager)
        elif choice == "10":
            financial_summary(manager)
        elif choice == "11":
            print("Exiting the program.............")
            break

def delete_transaction(manager):
    while True:
        try:
            transaction_id = int(input("Enter the transaction ID you want to delete: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid transaction ID.")
    transaction = manager.find_transaction_by_id(transaction_id)
    if transaction is None:
        print("Transaction not found")
        return
    success = manager.delete_transaction(transaction_id)
    if success:
        print("Transaction deleted successfully")
    else:
        print("Failed to delete transaction")
def financial_summary(manager):
    total_income = manager.calc_total_income()
    total_expenses = manager.calc_total_expenses()
    balance = manager.calc_balance()
    total_transactions = manager.total_transactions()
    income_transactions = manager.count_income_transactions()
    expense_transactions = manager.count_expense_transactions()
    print("\n=====Financial Summary=======:")
    print(f"Total Income: ₦{total_income:,.2f}")
    print(f"Total Expenses: ₦{total_expenses:,.2f}")
    print(f"Balance: ₦{balance:,.2f}")
    print(f"Total Transactions: {total_transactions}")
    print(f"Income Transactions: {income_transactions}")
    print(f"Expense Transactions: {expense_transactions}")
# Start the Finance Manager application

run_menu(manager)
