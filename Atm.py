class Atm:


    def __init__(self):
        self_pin=""
        self_balance=0
        self.menu()
    def menu(self):
        user_input=input("""
              Hello,How would you like to procceed?
              1.Enter 1 to create pin
              2.Enter 2 to deposit
              3.Enter 3 to withdraw
              4.Enter 4 to check balance
              5.Enter 5 to Exit
              """)
        if user_input=="1":
            self.CreatePin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.Withdraw()
        elif user_input=="4":
            print("check balance")
        else:
            print("byee")
    def CreatePin(self):
        self.pin=(input("enter the pin"))
        print("pin set successfully")
    def deposit(self):
        temp=int(input("Enter you pin"))
        if temp==self.pin():
            amount=int(input("Enter the amount"))
            self.balance=self.balance+amount
            print("deposit successful")
        else:
            print("invalid pin")
        
    def Withdraw(Self):
        temp=input("enter the pin")
        if temp==self.pin:
            amount=int(input("Enter the amount"))
            if amount<=self.balance:
                self.balance=self.balance-amount
                print("Operation successful")
            else:
                print("insufficient funds")
        else:
            print("invalid pin")
    def check_balance(self):
        temp=(input("Enter you pin"))
        if temp==self.pin:
            print(self.balance())
        else:
            print("invalid pin")
            
        
            
                
        
    
