class BankAccount:
	def __init__(self, name, accNo, bal = 500.0):
		self.name = name
		self.accNo = accNo
		self.balance = bal

	def getBalance(self):
		print("\nName = ", self.name)
		print("Account Number = ", self.accNo)
		print("Balance = ", self.balance)

	def deposit(self, dep):
		self.balance = self.balance + dep
		print(f"\n{dep} Rupees credited")

	def withdraw(self, withdraw):
		if self.balance > withdraw:
			self.balance = self.balance - withdraw
			print(f"\n{withdraw} Rupees debited")

		else:
			print("\nInsufficient funds")

	def checkBalance(self):
		print(f"\nYou have {self.balance} in your account.")

class SavingAccount(BankAccount):
	def __init__(self, name, accNo, bal, rate = 10):
		super().__init__(name, accNo, bal)
		self.balance = (self.balance/100) * rate

class CurrentAccount(BankAccount):
	def __init__(self, name, accNo, bal, overdraftLimit = 1000):
		super().__init__(name, accNo, bal)

	def checkBalance(self):
		print(f"You have {self.balance} in your account, and {overdraftLimit} as overdraft limit.")

	def withdraw(self, withdraw):
		if self.balance + self.overdraftLimit > withdraw:
			self.balance = self.balance - withdraw
			print(f"\n{withdraw} Rupees debited")

		else:
			print("\nInsufficient funds")

acc1 = BankAccount("Nice",1001, 10000)

acc1.checkBalance()
acc1.deposit(1000)
acc1.checkBalance()
acc1.withdraw(1000)
acc1.getBalance()

saveAcc1 = SavingAccount("NotNice", 1002, 2000)
saveAcc1.checkBalance()

currAcc1 = CurrentAccount("NotSoNice", 1003, 3000)
currAcc1.checkBalance()
