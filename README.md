# Personal Finance Manager

A Python-based command-line financial management application for recording, managing, and analyzing personal financial transactions.

The project was built with a focus on **Object-Oriented Programming, modular design, data validation, defensive programming, persistent storage, and user input handling**.

---

## Overview

The Personal Finance Manager is a command-line application built with Python that allows users to manage personal financial transactions through an interactive menu-driven interface.

Users can record income and expenses, view their transaction history, calculate financial summaries, search transaction descriptions, and filter transactions by category or transaction type.

The application uses a modular structure where transaction modeling, business logic, data persistence, and user interaction are separated into different components.

Transaction data is stored using JSON, allowing information to remain available between application sessions.

A major focus of the project was **data integrity and validation**. User input and saved transaction data are validated before being accepted by the application, while invalid or corrupted JSON data is handled without unnecessarily crashing the program.

---

## Key Features

### Transaction Management

* Create and store financial transactions
* Support for both income (`credit`) and expenses (`debit`)
* Transaction categories and descriptions
* Date-based transaction records
* Automatic persistence of transaction data

### Financial Analysis

* Calculate total income
* Calculate total expenses
* Calculate current balance
* View complete transaction history

### Search & Filtering

* Search transactions using descriptions
* Case-insensitive description searching
* Filter transactions by category
* Filter transactions by transaction type
* Case-insensitive filtering

### Input Validation

The application validates user input before processing transactions.

Validation includes:

* Numeric transaction amounts
* Positive transaction amounts
* Valid transaction types
* Non-empty categories
* Non-empty descriptions
* Valid date format
* Required transaction fields

### Defensive Data Handling

The application also checks data loaded from persistent storage.

It can detect:

* Missing `transactions.json`
* Invalid JSON
* Incorrect JSON structure
* Missing transaction fields
* Invalid transaction amounts
* Invalid transaction types
* Invalid transaction dates

This prevents invalid stored data from being silently accepted by the application's transaction model.

---

## Architecture

The application follows a simple modular architecture that separates responsibilities between different components.

```text
                    ┌──────────────────────┐
                    │       main.py        │
                    │  CLI / User Input    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  FinanceManager.py   │
                    │   Business Logic     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    transaction.py    │
                    │  Transaction Model   │
                    │     Validation       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      storage.py      │
                    │  Persistence Layer   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  transactions.json   │
                    │  Persistent Storage  │
                    └──────────────────────┘
```

### Design Responsibilities

**`main.py`**

Responsible for the command-line interface, menu navigation, user input, input validation, and interaction with the application's management layer.

**`FinanceManager.py`**

Acts as the application's management layer. It handles the transaction collection, financial calculations, searching, filtering, and preparing transaction data for storage.

**`transaction.py`**

Defines the `Transaction` data model and provides validation when transaction objects are created.

**`storage.py`**

Provides the persistence layer responsible for reading and writing transaction data and checking the basic structure of the stored JSON data.

**`transactions.json`**

Stores transaction records so that data can persist between application sessions.

---

## Project Structure

```text
Personal-Finance-Manager/
│
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

### Programming Language

* Python

### Core Concepts

* Object-Oriented Programming
* Classes and objects
* Class methods
* Modular programming
* File handling
* JSON serialization
* Data persistence
* Exception handling
* Input validation
* Defensive programming
* Searching and filtering
* Command-line interfaces

---

## Data Persistence

The application uses JSON-based persistence to maintain transaction data between sessions.

Transactions are converted from Python objects into dictionaries before being written to `transactions.json`.

When the application starts, saved dictionaries are loaded and converted back into `Transaction` objects.

```text
Transaction Object
        ↓
     to_dict()
        ↓
 Python Dictionary
        ↓
    JSON File
        ↓
   load_data()
        ↓
 Python Dictionary
        ↓
   from_dict()
        ↓
Transaction Object
```

This provides a simple persistence mechanism while keeping the transaction model and storage logic separated.

---

## Validation Strategy

Validation exists at multiple levels of the application.

### User Input Validation

The command-line interface validates information before creating transactions.

For example:

```text
Amount → Must be numeric and greater than 0
Type → credit or debit
Category → Cannot be empty
Description → Cannot be empty
Date → YYYY-MM-DD
```

### Model-Level Validation

The `Transaction` class independently validates transaction data when objects are created.

This provides an additional layer of protection because transaction objects do not rely only on validation performed by the command-line interface.

### Stored Data Validation

Data loaded from JSON is also checked before being converted into transaction objects.

The storage layer checks the basic JSON structure, while `Transaction.from_dict()` verifies that required transaction fields are present and that the values satisfy the transaction model's validation rules.

---

## Error Handling

The application uses Python exception handling to deal with invalid input and storage problems.

Examples include:

* Invalid numeric input
* Invalid dates
* Invalid transaction types
* Corrupted JSON
* Incorrect JSON structure
* Missing transaction fields
* Invalid saved transaction values

For certain storage-level problems, such as corrupted JSON or an invalid top-level JSON structure, the application displays a warning and continues with an empty transaction collection instead of immediately terminating.

---

## Testing

The application underwent structured manual testing covering both normal functionality and failure scenarios.

Testing included:

* Invalid transaction amounts
* Zero and negative amounts
* Invalid transaction types
* Empty categories
* Empty descriptions
* Invalid dates
* Invalid menu selections
* Invalid filters
* Empty searches
* Transaction creation
* Transaction persistence
* Multiple transaction storage
* Income calculations
* Expense calculations
* Balance calculations
* Category filtering
* Type filtering
* Description searching
* Case-insensitive searching
* Case-insensitive filtering
* Non-matching searches
* Corrupted JSON
* Incorrect JSON structure
* Missing transaction fields
* Invalid saved transaction values
* End-to-end application workflow

The testing process also helped identify and improve how the application handled malformed JSON and incomplete stored transaction data.

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
8. Exit

Enter your choice (1-8): 1

Enter amount: 15000
Enter the transaction type (credit/debit): debit
Enter the category for the transaction: Food
Enter the description of the transaction: Dinner
Enter the date: 2026-09-20

Transaction added successfully!
```

---

## Installation & Usage

### Requirements

* Python 3.x

### Clone the Repository

```bash
git clone <repository-url>
```

### Navigate into the Project

```bash
cd Personal-Finance-Manager
```

### Run the Application

```bash
python main.py
```

The application will launch through the command-line interface.

---

## Engineering Focus

This project was built to go beyond simply creating a working CLI application.

The development process focused on:

* Separating application responsibilities into modules
* Designing a reusable transaction model
* Validating data before persistence
* Protecting the application from malformed stored data
* Maintaining state between application sessions
* Building reusable management methods
* Handling invalid user input
* Testing both normal and failure scenarios
* Documenting the application's architecture and behavior

---

## Future Improvements

Potential improvements include:

* Transaction editing and deletion
* Monthly and yearly financial reports
* Category-based spending analytics
* Charts and data visualization
* Automated unit testing
* Database-backed persistence using MySQL or PostgreSQL
* User authentication
* CSV import and export
* Graphical user interface
* REST API
* Web-based version of the application

---

## Learning Outcomes

This project helped me improve my understanding of Python beyond just writing individual scripts.

I gained practical experience in:

* Designing Python applications using OOP
* Structuring applications into separate modules
* Working with persistent data
* Serializing and deserializing JSON
* Designing validation rules
* Handling exceptions
* Building interactive CLI applications
* Testing application behavior
* Debugging unexpected data conditions
* Thinking about data integrity and defensive programming
* Documenting software projects for version control and collaboration

---

## Project Status

**Status: Completed — CLI Version**

The current version provides a functional command-line financial management system with transaction management, financial calculations, searching, filtering, validation, JSON persistence, and defensive handling of invalid stored data.
