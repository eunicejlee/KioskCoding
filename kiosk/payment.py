class Payment():
    def __init__(self, paymentamount, discountamount):
        self.paymentamount=paymentamount
        self.discountamount=discountamount

    def __str__(self):
        self.paymentamount=round(self.paymentamount,2)
        response="Subtotal: " + str(self.paymentamount-self.discountamount)
        return response


