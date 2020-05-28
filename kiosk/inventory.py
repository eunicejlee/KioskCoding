from item import Item

class Inventory(Item):
    def __init__(self):
        self.items=[]
    
    def addItem(self, n):
        self.items.append(n)

    def getItems(self):
        return self.items
    
    def getItemByCode(self, code):
        reqItem=None
        for n in self.items:
            if n.itemcode==code:
                reqItem=n
                break
        return reqItem
