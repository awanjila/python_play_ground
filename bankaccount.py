class BankAccount:
	def __init__(self, balance): #Creates an account with the given balance.
		self.balance=balance
	def deposit(self, amount):
		self.balance +=amount  #Deposits some amount the into the account
	def withdraw(self, amount):
		if amount>self.balance:
			return "invalid transaction" #checks weather the amount wihde\wan is less than the balance
		else:
			self.balance-+amount
class MinimumBalanceAccount(BankAccount):
	def __init__(self):
		super(MinimumBalanceAccount,self). __init__() #ethod to show that minimumbalave MinimumBalanceAccount is a subclass of BankAccount