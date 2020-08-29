class Person(object):

    def __init__(self, fname,lname,email):
        self.first_name = fname
        self.last_name = lname
        self.email=email

    def firstName(self):
        return self.first_name

    def lastName(self):
        return self.last_name

    def emailAdress(self):
        return self.email
