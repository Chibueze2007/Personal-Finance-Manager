from transaction import Transaction
from storage import load_data,save_data

# Manage transactions and provide finance-related operations

class FinanceManager:

    # Initialize the transaction manager and load saved transactions

    def __init__(self):
        self.transactions=[]
        self.next_id = 1  # Initialize the next transaction ID
        self.load_transactions()

    # Add a new transaction to the transaction list

    def add_transaction(self,transaction):
        transaction.id = self.next_id # Assign the next available ID to the transaction
        self.transactions.append(transaction)
        self.next_id +=1

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
        for index,transaction_data in enumerate (data,start=1):
            if "id" not in transaction_data:
                transaction_data["id"] = index
            transaction= Transaction.from_dict(transaction_data)
            self.next_id = max(self.next_id, transaction.id + 1)  # Update next_id to be one more than the highest existing ID
            self.transactions.append(transaction)
            save_data(self.get_data())  # Save the updated data with IDs
    def find_transaction_by_id(self,transaction_id):
        for transaction in self.transactions:
            if transaction.id ==transaction_id:
                return transaction
        return None
    def edit_transactions(self,transaction_id,field,new_value):
        transaction = self.find_transaction_by_id(transaction_id)
        if transaction is None:
            return False
        amount = transaction.amount
        transaction_type = transaction.transaction_type
        category = transaction.category
        description = transaction.description
        date = transaction.date
        if field == "amount":
            amount = new_value
        elif field == "transaction_type":
            transaction_type = new_value
        elif field =="category":
            category = new_value
        elif field =="description":
            description = new_value
        elif field == "date":
            date = new_value
        updated_transaction = Transaction(
            amount,
            transaction_type,
            category,
            description,
            date,
            transaction.id
        )
        index = self.transactions.index(transaction)
        self.transactions[index] = updated_transaction
        save_data(self.get_data())
        return True
    def delete_transaction(self,transaction_id):
        transaction = self.find_transaction_by_id(transaction_id)
        if transaction is None:
            return False
        self.transactions.remove(transaction)
        save_data(self.get_data())
        return True
    def total_transactions(self):
        return len(self.transactions)
    def count_income_transactions(self):
        count = 0
        for transaction in self.transactions:
            if transaction.transaction_type == "credit":
                count += 1
        return count
    def count_expense_transactions(self):
            count = 0
            for transaction in self.transactions:
                if transaction.transaction_type == "debit":
                    count += 1
            return count
    