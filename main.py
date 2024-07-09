from classes import BankAccount

## Initialize the Bank Accounts using 
Bobs_Account = BankAccount("Bob",192910102,200)
Melindas_Account = BankAccount("Melinda",192914738,1200)

## Initial balance for bank accounts and info
print(Bobs_Account.display_account_info())

## Deposit, withdrawal, and get method called with 
print(Bobs_Account.deposit(2.00))
print(Bobs_Account.get_balance())
print(Bobs_Account.withdrawal(1.00))
print(Melindas_Account.deposit(223.00))
print(Melindas_Account.get_balance())
print(Melindas_Account.withdrawal(10.00))

## Error handling examples for overdrawing accounts and invalid input
print(Bobs_Account.withdrawal(1038.00))
print(Bobs_Account.withdrawal("one-hundred"))
print(Melindas_Account.deposit("Frank"))

## Print the Bank Account info for each Account after the methods are called to show results 
print(Melindas_Account.display_account_info())
print(Bobs_Account.display_account_info())

