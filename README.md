# Simple Bank Account Project

This project simulates a simple bank account system using object-oriented programming in Python. The project is divided into two files: `main.py` and `classes.py`.

## Project Structure

- `main.py`: This is the main script that runs the application.
- `classes.py`: This file contains the class definitions for the bank account system.

## Prerequisites

- Python 3.x

## How to Run

1. Clone or download the repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Run the main script:
    ```sh
    python main.py
    ```

## Classes

### BankAccount

This class represents a bank account with basic functionalities such as deposit, withdrawal, checking balance, and checking all account information.

#### Methods

- `__init__(self, accountHolder, accountNumber, balance)`: Initializes a new bank account with the given account holder's name: string, account number: integer, and starting balance: float.
- `get_balance(self)`: Returns the current balance of the account formatted to two decimal places.
- `deposit(self, amount)`: Deposits the specified amount into the account if it is a valid float. Returns the new balance or an error message for invalid input.
- `withdrawal(self, amount)`: Withdraws the specified amount from the account if it is a valid float and if there are sufficient funds. Returns the new balance, an error message for insufficient funds, or an error message for invalid input.
- `display_account_info(self)`: Returns the account holder's name, account number, and balance as a formatted string.

## Usage Example

To use this application, follow these steps:

1. **Create Bank Accounts in Main.py**:
    ```python
    from classes import BankAccount

    Bobs_Account = BankAccount("Bob", 192910102, 200)
    Melindas_Account = BankAccount("Melinda", 192914738, 1200)
    ```
2. **Run Main.py file**
```python
    py main.py
```