# Personal Finance Manager

A Python command-line application I built to help manage personal financial transactions.

I started this project to improve my Python skills and get more practical experience with **Object-Oriented Programming, file handling, JSON, validation, exception handling, and building applications with multiple files**.

The project started as a simple CLI application and was later improved with transaction IDs, editing, deleting, and a financial summary.

---

## Overview

The Personal Finance Manager allows users to record and manage income and expenses from the command line.

Users can:

* Add transactions
* View transactions
* Calculate total income
* Calculate total expenses
* Check the current balance
* Search transactions
* Filter transactions
* Edit transactions
* Delete transactions
* View a financial summary

The application stores transaction data in a JSON file, so the transactions are still available when the program is opened again.

One of the things I focused on while building the project was making sure invalid input was handled properly instead of allowing bad data into the application.

---

## Key Features

### Transaction Management

* Add income and expense transactions
* Assign categories and descriptions
* Store transaction dates
* Give each transaction a unique ID
* Edit existing transactions
* Delete transactions
* Save transactions to JSON

### Financial Calculations

* Calculate total income
* Calculate total expenses
* Calculate current balance
* View a financial summary
* Count total transactions
* Count income transactions
* Count expense transactions

### Search & Filtering

* Search transactions by description
* Filter transactions by category
* Filter transactions by transaction type
* Case-insensitive searching and filtering

### Input Validation

The application checks user input before accepting it.

Some of the validation includes:

* Amount must be a number
* Amount must be greater than 0
* Transaction type must be `credit` or `debit`
* Category cannot be empty
* Description cannot be empty
* Date must follow the `YYYY-MM-DD` format
* Transaction IDs must be valid when editing or deleting

### JSON Data Validation

The application also checks data loaded from `transactions.json`.

It handles things such as:

* Missing JSON file
* Invalid JSON
* Incorrect JSON structure
* Missing transaction fields
* Invalid saved transaction values

---

## How the Project is Organized

I separated the project into different files so that each file has a specific responsibility.

```text
                    ┌──────────────────────┐
                    │       main.py        │
                    │  User Interaction    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  FinanceManager.py   │
                    │   Main Logic         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    transaction.py    │
                    │ Transaction Model     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      storage.py      │
                    │ JSON Storage         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  transactions.json   │
                    │ Saved Data            │
                    └──────────────────────┘
```

### `main.py`

Handles the menu, user input, and functions that interact with the user.

### `FinanceManager.py`

Contains most of the application's main logic.

It handles adding, editing, deleting, searching, filtering, calculating totals, and managing transaction IDs.

### `transaction.py`

Contains the `Transaction` class.

This is where the transaction data is created and validated.

### `storage.py`

Handles loading and saving data from the JSON file.

### `transactions.json`

Stores the transaction data so it can be loaded again when the application starts.

---

## Project Structure

```text
Personal-Finance-Manager/

├── main.py
├── transaction.py
├── FinanceManager.py
├── storage.py
├── transactions.json
├── .gitignore
└── README.md
```

---

## Technologies & Concepts

### Language

* Python

### Concepts Used

* Object-Oriented Programming
* Classes and objects
* Class methods
* Functions
* Modular programming
* File handling
* JSON
* JSON serialization and deserialization
* Data persistence
* Exception handling
* Input validation
* Searching and filtering
* CRUD operations
* Command-line interfaces

---

## How Data is Saved

The project uses JSON to save transactions.

When a transaction is created, it is converted into a dictionary before being saved.

When the program starts again, the saved data is loaded and converted back into `Transaction` objects.

The basic flow is:

```text
Transaction Object
        ↓
     to_dict()
        ↓
     Dictionary
        ↓
 transactions.json
        ↓
    load_data()
        ↓
     Dictionary
        ↓
   from_dict()
        ↓
Transaction Object
```

Transaction IDs are also saved in the JSON file so that an existing transaction keeps the same ID after restarting the program.

---

## Validation

I added validation in different parts of the application.

### User Input

For example:

```text
Amount → Must be a number and greater than 0
Type → credit or debit
Category → Cannot be empty
Description → Cannot be empty
Date → YYYY-MM-DD
```

### Transaction Model

The `Transaction` class also validates the data when a transaction object is created.

This means the data is not only checked in the CLI. The model also has its own validation.

### Saved Data

Data loaded from the JSON file is also checked.

For example, if a required field is missing or an invalid value is stored, the `Transaction` class can reject it.

---

## Error Handling

I used Python's exception handling to deal with invalid input and other problems.

Some examples include:

* Invalid numbers
* Invalid dates
* Invalid transaction types
* Invalid transaction IDs
* Corrupted JSON
* Incorrect JSON structure
* Missing transaction fields
* Invalid saved transaction values

---

## Testing

I manually tested the application throughout the development process.

Some of the tests included:

* Adding transactions
* Adding multiple transactions
* Invalid amounts
* Zero and negative amounts
* Invalid transaction types
* Empty categories
* Empty descriptions
* Invalid dates
* Searching transactions
* Searching for something that doesn't exist
* Filtering by category
* Filtering by transaction type
* Case-insensitive searching
* Case-insensitive filtering
* Checking income
* Checking expenses
* Checking balance
* Editing transactions
* Editing invalid values
* Editing a transaction that doesn't exist
* Checking that edited data remains after restarting
* Deleting transactions
* Deleting a transaction that doesn't exist
* Checking that deleted data remains deleted after restarting
* Checking transaction IDs
* Financial summary
* Financial summary with no transactions
* Corrupted JSON
* Missing transaction fields
* End-to-end testing

The testing helped me find and fix several issues while developing the project.

---

## Example

```text
========PERSONAL FINANCE MANAGER=====

1. Add Transaction
2. View Transactions
3. View Total Income
4. View Total Expenses
5. View Current Balance
6. Search Transactions by Description
7. Filter Transactions by Category or Transaction Type
8. Edit Transactions
9. Delete Transaction
10. View Financial Summary
11. Exit

Enter your choice (1-11): 10

=====Financial Summary=======:
Total Income: ₦150,000.00
Total Expenses: ₦45,000.00
Balance: ₦105,000.00
Total Transactions: 5
Income Transactions: 2
Expense Transactions: 3
```

---

## Installation & Usage

### Requirements

* Python 3.x

### Clone the Repository

```bash
git clone <repository-url>
```

### Enter the Project Folder

```bash
cd Personal-Finance-Manager
```

### Run the Application

```bash
python main.py
```

The application will then start in the terminal.

---

## What I Focused On

While building this project, I focused on more than just making the program work.

I wanted to understand how to:

* Break a Python project into different files
* Use classes and objects properly
* Store data outside the program
* Validate user input
* Handle errors
* Work with JSON
* Keep data after restarting the program
* Add, edit, and delete records
* Debug problems as they came up
* Test different situations instead of only testing the normal case

---

## Future Improvements

Some of the things I plan to add in future versions are:

* Tkinter GUI
* Monthly and yearly financial reports
* Spending analytics
* Charts and data visualization
* Bank statement feature
* Automated tests
* MySQL or PostgreSQL database
* User registration and login
* CSV import and export
* REST API
* Web version

---

## What I Learned

This project helped me understand Python better because I had to use several concepts together instead of writing small standalone programs.

I got more practice with:

* Object-Oriented Programming
* Classes and objects
* Modular programming
* JSON
* File handling
* Data validation
* Exception handling
* Persistent data
* CRUD operations
* Debugging
* Testing
* Git and GitHub

I also learned that getting a program to work is only part of building a project. I had to think about what happens when the user enters something unexpected or when the saved data is not what the program expects.

---

## Project Status

**V2 Completed — CLI Version**

The current version has transaction management, persistent transaction IDs, editing and deleting transactions, financial calculations, financial summaries, searching, filtering, input validation, and JSON persistence.

The next major version will focus on building a GUI and adding more financial analysis features.
