class Atm:

    def __init__ (self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin  

    def check_balance(self):
        print ("Your balance is 50000")

    def cashWithdrawal(self):
        print ("Your balance is 50000")

    def balanceEnquiry(self):
        print ("Your balance is 50000")

new_user = Atm (1,5)

new_user.check_balance ()
new_user.cashWithdrawal ()
new_user.balanceEnquiry ()