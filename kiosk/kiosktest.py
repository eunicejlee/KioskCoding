import unittest
from customer import Customer
from item import Item
from department import Department
from inventory import Inventory
from purchaseitem import PurchaseItem
from payment import Payment
from checkout import Checkout

#firstname, lastname, phone, address, city, state, zipcode
class CustomerTest(unittest.TestCase):
    def setUp(self):
        self.customer=Customer('Eunice', 'Lee', '2067421235', '4201 University Way NE', 'Seattle', 'WA', '98105')
    
    def test_customerstring(self):
        self.assertEqual(str(self.customer), self.customer.firstname)

class ItemTest(unittest.TestCase):
    def setUp(self):
        self.item=Item(4206, 'Green Onion', 0.89)

    def test_getItemCode(self):
        self.assertEqual(str(self.item.getItemCode()), '4206')

    def test_getItemName(self):
        self.assertEqual(str(self.item), self.item.itemname)

    def test_getItemPrice(self):
        self.assertEqual(str(self.item.getItemPrice()), '0.89')

class DepartmentTest(unittest.TestCase):
    def setUp(self):
        self.department=Department('produce')

    def test_getDeptName(self):
        self.assertEqual(str(self.department.getDeptName()), 'produce')

class InventoryTest(unittest.TestCase):
    def setUp(self):
        self.item1=Item(4206, 'Green Onion', 0.89)
        self.item2=Item(4131, 'Fuji Apple', 1.99)
        self.item3=Item(4011, 'Banana', 0.79)

        #add items
        self.inven=Inventory()
        self.inven.addItem(self.item1)
        self.inven.addItem(self.item2)
        self.inven.addItem(self.item3)

    def test_getItems(self):
        items=self.inven.getItems()
        self.assertEqual(len(items),3)

    def test_getItemByCode(self):
        item=self.inven.getItemByCode(4011)
        self.assertEqual(str(item),'Banana')

class PurchaseItemTest(unittest.TestCase):
    def setUp(self):
        self.purchaseitem=PurchaseItem(4011, 'Banana')
        self.quantity=5
        self.purchaseitem=PurchaseItem(self.item, self.quantity)

    def test_getItem(self):
        self.item=self.purchaseitem.getItem()
        self.assertEqual(str(self.item), 'Banana')
        
    def test_getQuantity(self):
        self.assertEqual(self.purchaseitem.getQuantity(), 5)

class CheckoutTest(unittest.TestCase):
    def setUp(self):
        self.o=Checkout()
        self.item1=Item(4206, 'Green Onion', 0.89)
        self.item2=Item(4131, 'Fuji Apple', 1.99)
        self.item3=Item(4011, 'Banana', 0.79)

        self.purchaseitem1=PurchaseItem(self.item1,2)
        self.purchaseitem2=PurchaseItem(self.item2,4)
        self.purchaseitem3=PurchaseItem(self.item3,3)

        self.o.addPurchaseItems(self.purchaseitem1)
        self.o.addPurchaseItems(self.purchaseitem2)
        self.o.addPurchaseItems(self.purchaseitem3)

    def test_addandgetPurchaseItems(self):
        self.oitems=self.o.getPurchaseItems()
        self.assertEqual(len(self.oitems),3)

    def test_CalculateTotal(self):
        payment=self.o.calcTotal()
        self.assertEqual(str(payment), 'Subtotal: 13.89')