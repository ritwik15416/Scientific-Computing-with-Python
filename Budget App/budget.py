ledger = []
bal = 0
draw = False
class Category:
    def __init__(self,categ):
        self.categ = categ
    def deposit(self,amt,desc=""):
        global bal
        ledger.append({"description": desc, "amount": amt})
        bal += amt
    def withdraw(self,amt,desc=""):
        global bal
        bal -= amt
        if bal >= 0:
            ledger.append({"description": desc,"amount": "-"+str(amt)})
            draw = True
        else:
            draw = False
            bal += amt
        return draw
    def get_balance(self):
        if bal > 0:
            return bal
        else:
            return 0
    def transfer(self,amt,cat):
        global bal
        descw = "Transfer to " + cat
        yes = self.withdraw(amt,descw)
        if yes == True:
            descd = "Transfer from "+ self.categ
            self.deposit(amt,descd)
            bal -= amt
            return yes
        else:
            return False
    def printer(self):
        print("*********"+self.categ+"*********\n")
        for i in ledger:
            entry = i["description"] + "\t" + str(i["amount"])
            print(entry)
        print("Total:\t",bal)



        
        
        
        
