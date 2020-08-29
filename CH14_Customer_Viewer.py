# Hayoung Nam
# July 12 2020
# Customer Viewer
# Create an object-oriented program allows the user to display the data for a customer by specifying the customer's ID using the format shown below.

import csv

class Customer():
    
    def __init__(self,cust_id,firstName,lastName,company,address,city,state,zip):
        self.cust_id=cust_id
        self.first_name=firstName
        self.last_name=lastName
        self.company_name=company
        self.address=address
        self.city=city
        self.state=state
        self.zip=zip

    def __str__(self):
        str=""
        if self.company_name=="":
            str+=self.first_name+" "+self.last_name+"\n"+self.address+"\n"+self.city+", "+self.state+" "+self.zip
        else:
            str+=self.first_name+" "+self.last_name+"\n"+self.company_name+"\n"+self.address+"\n"+self.city+", "+self.state+" "+self.zip
        return str


# Main

customerList=[]

with open("Customers.csv", "r") as FILENAME:
    reader = csv.reader(FILENAME)
    for line in reader:
        customerList.append(Customer(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]))


    customerList.pop(0)

    print("Customer Viwer")
    print ("\nEnter the customer ID to view the customer address")


    while True:
        id=input("\nEnter customer ID: ")
        count=0

        for customer in customerList:
            if(customer.cust_id==id):
                print()
                print(customer)
                print()
                count=1
                break

        if(count==0):
            print("No customer with that ID.\n")

        choice=input("Continue? (y/n): ")

        if (choice == "Y" or choice == "y"):
            continue

        if(choice=="N" or choice=="n"):
            print ("\nBye!") 
            quit ()
        else:
            print ("ERROR - Invalid. Try again")
            continue  
