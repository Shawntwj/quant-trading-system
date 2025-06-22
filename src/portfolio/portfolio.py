class Portfolio: 
    def __init__(self, initialCash = 66000):
        self.balance = initialCash
    
    def getCashBalance(self):
        return self.balance 
    
    def addCash(self, amount):
        self.balance += amount
        return self.balance 
    
    def canAfford(self, amount):
        return amount <= self.balance
    
    def __str__(self):
        return str(self.balance)
