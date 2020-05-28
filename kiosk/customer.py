class Customer():
    def __init__(self, firstname, lastname, phone, address, city, state, zipcode):
        self.firstname=firstname
        self.lastname=lastname
        self.phone=phone
        self.address=address
        self.city=city
        self.state=state
        self.zipcode=zipcode

    def getFirstname(self):
        return self.firstname

    def getLastname(self):
        return self.lastname

    def getPhone(self):
        return self.phone
    
    def getAddress(self):
        return self.address
    
    def getCity(self):
        return self.city
    
    def getState(self):
        return self.state
    
    def getZipcode(self):
        return self.zipcode

    def __str__(self):
        return "Welcome" + self.firstname + " " + self.lastname