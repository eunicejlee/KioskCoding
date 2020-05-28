from department import Department

class Item():
    def __init__(self, itemcode, itemname, itemprice):
        self.itemcode=itemcode
        self.itemname=itemname
        self.itemprice=itemprice

    def getItemCode(self):
        return self.itemcode

    def getItemName(self):
        return self.itemname

    def getItemPrice(self):
        return self.itemprice

    def __str__(self):
        return str(self.itemcode) + ' '+ self.itemname + ' ' + self.itemprice