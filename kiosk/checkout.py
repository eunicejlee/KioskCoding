from item import Item
from purchaseitem import PurchaseItem
from payment import Payment

class Checkout():
    def __init__(self):
        self.purchaseitems=[]

    def addPurchaseItems(self, purchaseitem):
        self.purchaseitems.append(purchaseitem)

    def getPurchaseItems(self):
        return self.purchaseitems

    def calcTotal(self):
        total=0.0
        for o in self.purchaseitems:
            total += o.getItem().itemprice * o.quantity
        payment=Payment(total)
        return payment