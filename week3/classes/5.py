'''Create a bank account class that has attributes owner, 
balance and two methods deposit and withdraw. Withdrawals 
may not exceed the available balance. Instantiate your class, 
make several deposits and withdrawals, and test to make sure the account can't be overdrawn.'''

class Account:
	def __init__(self):
		self.balance=0

	def deposit(self):
		amount=float(input("Enter amount to be Deposited: "))
		self.balance += amount
		print("Amount Deposited:",amount)

	def withdraw(self):
		amount = float(input("Enter amount to be Withdrawn: "))
		if self.balance>=amount:
			self.balance-=amount
			print("You Withdrew:", amount)
		else:
			print("Insufficient balance")

	def balancenow(self):
		print("Available Balance=",self.balance)

s = Account()

s.deposit()
s.withdraw()
s.balancenow()
