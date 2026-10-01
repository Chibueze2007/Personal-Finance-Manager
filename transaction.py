from datetime import datetime 


# created the class Transaction
class Transaction:
    def __init__(self,amount,transaction_type,category,description,date,id=None):


        # condition so that amount is a number
        if not isinstance(amount,(int,float)):
            raise ValueError("Amount must be in int or float")
        # condition so that amount is not <=0
        if amount <= 0:
            raise ValueError("Amount should be greater than 0")
        # condition for invalid transaction type tuple was used instead of list because i want it to be immutable
        if transaction_type.strip().lower() not in ("credit","debit"):
            raise ValueError("Transaction type should be either credit or debit")
        transaction_type = transaction_type.strip().lower()
        self.transaction_type = transaction_type
        # condition to protect itself against empty category 
       
        if not category.strip():
            raise ValueError("Category cannot be empty")
        # condition to protect itself from empty description 
        if not description.strip():
            raise ValueError("Description cannot be empty")
        category = category.strip()
        description = description.strip()
        # condition to validate date 
        try:
            datetime.strptime(date,"%Y-%m-%d")
        except ValueError:
            raise ValueError("Incorrect date format")
        self.id = id
        self.amount= amount
        self.category = category
        self.description = description
        self.date = date

    # Define how a transaction object should be displayed when printed
    def __str__(self):
        return f"ID: {self.id} | {self.transaction_type.capitalize()} | {self.category.capitalize()} | {self.description.capitalize()} | ₦{self.amount:,} | {self.date}"


    # Convert the transaction object into a dictionary for JSON storage
    def to_dict(self):
        return{
            "id":self.id,
            "amount":self.amount,
            "transaction_type":self.transaction_type,
            "category":self.category,
            "description": self.description,
            "date":self.date,
            
        }
    # Create a Transaction object from saved dictionary data
   
    @classmethod
    def from_dict(cls,data):

        # List of fields that must be present in the saved transaction data

        required_fields = [
            "amount",
            "transaction_type",
            "category",
            "description",
            "date"
        ]

        # Check that all required fields are present

        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        # Recreate the transaction using the saved data
        
        return cls(
            data["amount"],
            data["transaction_type"],
            data["category"],
            data["description"],
            data["date"],
            data["id"]
        )