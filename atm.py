"""
Create a python class ATM which has a parametrised constructor (card_no, acc_balance).
Create methods withdraw(amount) which should check if the amount is available on the
account if yes, then deduct the amount and print the message “Amount withdrawn”, if the
amount is not available then print the message “OOPS! Unable to withdraw amount, Low
balance”. Create another method called, deposit, which should deposit amount if amount is
positive and should print message “Amount deposited”. If not, print message “Invalid amount
to deposit”. Create a method called getBalance which should print current balances at any
given point of time.
           Example: atm_acc_1 = ATM(“1234”, 400)
           atm_acc_2 = ATM(“10001”, 100)
"""
class ATM:
    #constructor of ATM,
    def __init__(self,card_no, acc_balance):
        self.card_no = card_no
        self.acc_balance = acc_balance

    #amount withdraw func, if balance >= amount
    def withdraw(self,amount):
        if self.acc_balance >= amount:
            self.acc_balance = self.acc_balance - amount
            print("Message: Amount withdrawn")
        else:
            print("Message: OOPS! Unable to withdraw amount, Low balance")

    #deposit the given amount
    def deposit(self,deposit_amount):
        if deposit_amount>0:
            self.acc_balance = self.acc_balance + deposit_amount
            print("Message: Amount deposited")
        else:
            print("Message: Invalid amount to deposit")

    #get the balance amount for us
    def getBalance(self):
        print("Current Balance:",self.acc_balance)

atm_acc_1 = ATM("1234",400)
atm_acc_2 = ATM("10001",100)

print("Account :",atm_acc_1.card_no)
print("----------------------------")
atm_acc_1.withdraw(300)
atm_acc_1.withdraw(300)
atm_acc_1.deposit(300)
atm_acc_1.getBalance()

print("\nAccount :",atm_acc_2.card_no)
print("----------------------------")
atm_acc_2.getBalance()
atm_acc_2.deposit(300)
atm_acc_2.getBalance()


"""
Output:
/GitHub/talentpy-Assgn5/atm.py
Account : 1234
----------------------------
Message: Amount withdrawn
Message: OOPS! Unable to withdraw amount, Low balance
Message: Amount deposited
Current Balance: 400

Account : 10001
----------------------------
Current Balance: 100
Message: Amount deposited
Current Balance: 400
"""