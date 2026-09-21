import json
import os
# Save transaction data to the JSON file
def save_data(data):
    with open ("transactions.json","w") as file:
        json.dump(data,file,indent=4)
# Load transaction data from the JSON file
def load_data():
    if os.path.exists("transactions.json"):
        with open("transactions.json","r") as file:
            try:
                data = json.load(file)
                # Make sure the saved data is stored as a list
                if isinstance(data,list):
                    return data
                else:
                    print("Warning : transactions.json must contain a list")
                    return []
                # Handle invalid or corrupted JSON data
            except json.JSONDecodeError:
                print("Warning : The transactions.json contains invalid data.")
                return []
    # Return an empty list if the file does not exist
    else:
        return []