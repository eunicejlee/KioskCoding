from customer import Customer 

class Member():
    def __init__(self, firstname, phone):
        self.firstname=firstname
        self.phone=phone

    def __str__(self):
        return super(Member, self) .__str__()