class Atm:

    def __init__(self):
        self.pin = ""
        self.balance = 0

        self.menu()

    def menu(self):
        user_input = input("""

       Hello , how would you like to proceed:
       1.Enter 1 to create pin
       2.Enter 2 to deposit
       3.Enter 3 to withdraw
       4.Enter 4 to check balance
       5.Enter 5 to exit 
    
    """)    

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("exiting")

def create_pin(self):
    self.pin = int(input("Create a pin"))
    print("pin created successfully!")
    self.menu()

def deposit(self):
    temp = int(input("Deposit Money: "))
    if temp == self.pin:
        amount = int(input("Enter the amount: "))
        if amount <= self.balance:
            self.balance = self.balance + amount
            print("deposit successfully")
        else:
            print("Invalid pin")
def withdraw(self):
    temp = int(input("Deposit Money: "))
    if temp == self.pin:
        amount = int(input("Enter the amount: "))
        if amount < self.balance:
            self.balance = self.balance - amount
            print("Withdraw Successfully")
        else:
            print("Insufficient funds")
    else:
        print("invalid pin")

def check_balance(self):
    temp = input("enter your pin")
    if temp == self.pin:
        print(self.balance)
    else:
        print("invalid pin")

