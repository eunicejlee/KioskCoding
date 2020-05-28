from item import Item

class PurchaseItem():
    def __init__(self,item,quantity):
        self.item=item
        self.quantity=quantity
    
    def getItem(self):
        return self.item

    def getQuantity(self):
        return self.quantity
