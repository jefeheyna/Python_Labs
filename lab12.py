#--------------------------------------------------------------------------------------------------
#Jeff Hejna
#12/1/2014
#Lab 12
#
#The purpose of this program is to create fake credit cards that can be charged and such.
#
#                           Algorithm
#               1)Create credit card information
#               2)Allow card to be charged, pay balance, charge interest,and transfer balances
#
#--------------------------------------------------------------------------------------------------




import random

class CreditCard:
    def __init__(self,nameIn,cardNumber,creditScore):
        '''This function creates the credit cards and info along with it.'''
        self.name = nameIn
        self.cardnumber = cardNumber
        self.creditscore = creditScore
        self.balance = 0
        if creditScore>750:
            self.limit = 10000
            self.apr = 8
        elif creditScore>=600 and creditScore<=750:
            self.limit = 5000
            self.apr = 12
        elif creditScore<600:
            self.limit = 2000
            self.apr = 20

    def displayAccount(self):
        '''This function displays the info for each credit card.'''
        print('Name: ',self.name)
        print('Card Number: ',self.cardnumber)
        print('Credit Score: ',self.creditscore)
        print('Credit Limit: ',self.limit)
        print('APR: ',self.apr,'%')
        print('Balance: ',self.balance)


    def charge(self,charge):
        '''This function allows the credit card to be charged a certain amount.'''
        if charge+self.balance>self.limit:
            print("Denied. You have exceeded your credit limit.")
            return False
        elif charge<0:
            print("Error. Charge cannot be less than 0.")
            return False
        elif charge+self.balance<=self.limit:
            self.balance+=charge
            print("Balance: ",self.balance)
            
            
    def payBalance(self,payment):
        '''This funtion allows for the balance to be payed.'''
        if payment<0:
            print("Error. Payment amount cannot be less than 0.")
            return False
        else:
            self.balance-=payment
            print("Balance: ",self.balance)

    def transferFunds(self,dest,amount):
        '''This function transfers the balance from one card to another.'''
        if amount<=self.balance and amount>=0:
            temp=dest.transferTo(amount,self.cardnumber)
            if temp:
                self.balance-=amount
                return True
            else:
                print("Sorry the transfer could not be completed.")
                print()
                return False
        else:
            return False

    def transferTo(self,amount,accnt):
        '''This funtion adds the amount transfered to the other card.'''
        if self.balance+amount<=self.limit:
            self.balance+=amount
            return True
        else:
            return False

    def interest(self):
        '''This function calculates and adds the interest to the balance.'''
        if self.balance>=0:
            interest=(self.apr/100)*self.balance
            print("Amount of interest accrued: ",interest)
            print()
            print("Balance: ",self.balance+interest)
            print()
            self.balance+=interest
        else:
            print("No interest accrued. This is your balance: ",self.balance)


def main():
    '''This is the main funtion that runs the whole program.'''
    card1=random.randrange(1000000000000000,9999999999999999)
    card2=random.randrange(1000000000000000,9999999999999999)

    account1=CreditCard("Bob Smith",card1,800)
    account2=CreditCard("Joe",card2,650)

    account1.displayAccount()
    print()
    account2.displayAccount()
    print()

    print("Charging Account 1:")
    account1.charge(8000)
    print()
    print("Charging Account 2:")
    account2.charge(5000)
    print()

    print("Paying Balance of Account 1:")
    account1.payBalance(200)
    print() 
    print("Paying Balance of Account 2:")
    account2.payBalance(10)
    
    print()
    print("Interest for Account 1:")
    account1.interest()
    print()
    print("Interest for Account 2:")
    account2.interest()
    print()
    
    
    print("After transfering funds from Account 2 to Account 1:")
    account2.transferFunds(account1,account2.balance)
    account1.displayAccount()
    print()
    account2.displayAccount()
  
main()            
            
        
