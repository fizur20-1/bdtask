from abc import ABC, abstractmethod

class Bank(ABC):
    def __init__(self):
        self.CurrentBalance = 0

    def deposit(self, Amount):
        if Amount > 0:
            self.CurrentBalance += Amount
            print('Deposited amount :')
            print (Amount)
        else:
            print("TOO short Amount to Deposit")

    def withdraw(self, Amount):
        if Amount > 0 and self.CurrentBalance > Amount:
            self.CurrentBalance = self.CurrentBalance - Amount
            print('Withdraw amount is :')
            print(Amount)
        else:
            print("Enter wrong amount, TRY AGAIN! .")

    @abstractmethod
    def get_balance(self):
        pass

class SavingAccount(Bank):
    def __init__(self):
        super().__init__()
        self.InterestRate = 0.05

    def CalculateInterest(self):
        interest = self.CurrentBalance * self.InterestRate
        self.CurrentBalance+=interest
        print("Total Interest accrued:" )
        print(interest)

    def get_balance(self):
        print("After adding interest Current balance: ")
        print(self.CurrentBalance )

class CheckingAccount(Bank):
    def __init__(self):
        super().__init__()
        self.Threshold = 1000
        self.count=0

    def withdraw(self, amount):
        if amount > 0 and self.CurrentBalance -amount >= self.Threshold:
            self.count=0
            self.CurrentBalance -= amount
            print("Withdrew amount :")
            print (amount)
        else:
            self.count=1
            print("Not allowed to withdraw this much amount !")

    def get_balance(self):
        if self.count>0:
             print("No withdrawl ! and Current balance:" ) 
             print(self.CurrentBalance)
        else :
            print("After withdrawl !  Current balance:" )
            print(self.CurrentBalance)


savings = SavingAccount()
savings.deposit(1000) 
savings.CalculateInterest() 
savings.get_balance()

checking = CheckingAccount()
checking.deposit(500)
checking.get_balance()  
checking.withdraw(800)  
checking.get_balance()  