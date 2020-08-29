from person import Person
class Customer(Person):
    def __init__(self, fname,lname,emailAdress,number):
        Person.__init__(self, fname, lname, emailAdress)
        self.customer_number=number

    def customerNumber(self):
        return self.customer_number
