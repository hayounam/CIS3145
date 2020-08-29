from person import Person

class Employee(Person):
    def __init__(self, fname,lname,emailAdress,ssn):
        Person.__init__(self, fname, lname, emailAdress)
        self.SSN=ssn

    def socialNumber(self):
        return self.SSN
