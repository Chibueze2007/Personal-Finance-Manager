from transaction import Transaction
from storage import load_data

# Manage transactions and provide finance-related operations

class FinanceManager:

    # Initialize the transaction manager and load saved transactions

    def __init__(self):
        self.transactions=[]
        self.load_transactions()

    # Add a new transaction to the transaction list

    def add_transaction(self,transaction):
        self.transactions.append(transaction)

        # Display all stored transactions
    def view_transactions(self):
        if not self.transactions:
            print("No transactions available")
            return
        
        for transaction in self.transactions:
            print(transaction)

    # Calculate the total amount of all credit transactions

    def calc_total_income(self):
        total = 0
        for transaction in self.transactions:
            if transaction.transaction_type =="credit":
                total +=transaction.amount
        return total

    # Calculate the total amount of all debit transactions

    def calc_total_expenses(self):
        total = 0
        for transaction in self.transactions:
            if transaction.transaction_type=="debit":
                total+=transaction.amount
        return total
    
    # Calculate the current balance by subtracting expenses from income
    
    def calc_balance(self):
        income = self.calc_total_income()
        expense = self.calc_total_expenses()
        balance = income - expense
        return balance

    # Display transactions that match the specified category

    def filter_by_category(self,category):
        found = False
        for transaction in self.transactions:
            if transaction.category.lower() == category.lower():
                print(transaction)
                found = True
        if not found:
            print("No transactions found")

    # Display transactions that match the specified transaction type

    def filter_by_type(self,transaction_type):
        found = False
        for transaction in self.transactions:
            if transaction.transaction_type.lower() == transaction_type.lower():
                print(transaction)
                found = True
        if not found:
            print("No transactions found")

    # Search for transactions using part of their description

    def search_by_description(self,search_term):
        found = False
        for transaction in self.transactions:
            if search_term.lower() in transaction.description.lower():
                print(transaction)
                found = True
        if not found:
            print("No transactions found")

    # Convert all transactions into dictionaries for JSON storage

    def get_data(self):
        data = []
        for transaction in self.transactions:
            data.append(transaction.to_dict())
        return data
    # Load saved transaction data and recreate Transaction objects

    def load_transactions(self):
        data = load_data()
        for transaction_data in data:
            transaction= Transaction.from_dict(transaction_data)
            self.transactions.append(transaction)