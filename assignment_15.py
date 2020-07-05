class Customer:
    from random import randint
    n = 10
    start = 10**(n-1)
    end = 10**n -1
    def __init__(self, firstName, lastName, balance = 0):
        self.firstName = firstName
        self.lastName = lastName
        self.balance = balance
        self.account_number = self.__class__.randint(self.__class__.start, self.__class__.end)

    def show_info(self):
        print('\nCustomer Detail:')
        print('Full Name:',self.firstName, self.lastName)
        print('Account number:',self.account_number)

    def deposit(self, amount):
        print(f'\nDepositing {amount}...')
        self.balance += amount
    
    def withdraw(self, amount):
        print(f'\nwithdrawing {amount}...')
        self.balance -= amount

    def balance_inquiry(self):
        print('\nTotal balance:',self.balance)

customer_1 = Customer('Ram', 'Dhakal')
customer_1.show_info()
customer_1.balance_inquiry()
customer_1.deposit(20000)
customer_1.balance_inquiry()
customer_1.withdraw(5000)
customer_1.balance_inquiry()