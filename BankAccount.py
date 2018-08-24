import time

# Creating the bank account class.
class BankAccount():

    # Calling the __init__ constructor and assigning attributes to variables
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    # Method to provide account details
    def acc_info(self):
        print('Account owner: {}'.format(self.owner))
        print('Account balance: {}'.format(self.balance))
        
    # Method to deposit a particular amount
    def deposit(self, amount_to_deposit):
        self.amount_to_deposit = amount_to_deposit


        print('You have added {} to your account.'.format(amount_to_deposit))

        self.balance = self.balance + amount_to_deposit
        
      
    # Method to withdra from whatever funds are available
    def withdraw(self, amount_to_withdraw):


        time.sleep(2)
        print('The total amount of money you have is {}'.format(self.balance))

        if self.balance < amount_to_withdraw:
            print('Funds Unavailable.')
        else:
            print('you can withdraw from {}'.format(self.balance))


# Object creation
acct1 = BankAccount('Jose', 100)
acct2 = BankAccount('Jordan', 150)

# print(acct1.owner)
# print(acct1.balance)
# acct1.acc_info()

acct2.deposit(50)

time.sleep(2)
print('And your total is {}'.format(acct2.balance))


time.sleep(2)
acct2.withdraw(int(input('Enter the amount you want to withdraw: ')))



