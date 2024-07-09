class BankAccount():
    def __init__(self, accountHolder,accountNumber, balance):
        self._accountHolder = str(accountHolder)
        self.__balance = float(balance)
        self._accountNumber = str(accountNumber)

    def get_balance(self):
        return( f" {self.__balance:.2f}")

    def deposit(self, amount):
        if type(amount) == float:
            self.__balance = amount + self.__balance
            return(self.__balance)
        else:
           return("Enter a valid dollar input ex. 200.00")
    ## Returns the balance after the $ amount passed into function is subtracted from the current balance, if the balance is less than the amount being withdrawn it returns a insufficient funds message or if the amount isn't a float it returns invalid input
    def withdrawal(self, amount):
        if type(amount) == float:
           if (self.__balance < amount):
                return("Insufficient Funds")  
           else:
                self.__balance = self.__balance - amount
                return(self.__balance) 
        else:
             return("Enter a valid dollar input ex. 200.00")
    # Returns the account name, number, and balance in a formated string
    def display_account_info(self):
        return (f"{self._accountHolder}, your current balance for account number {self._accountNumber} is ${self.__balance:.2f}")
            