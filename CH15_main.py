# Hayoung Nam
# July 15 2020
# Customer Employee Creater
# Create an object-oriented program that allows to enter data for customers and employees. 
from person import Person
from employee import Employee
from customer import Customer

    
def main():
    print ("Customer/Employee Data Entry\n") 
    while True:
        option=input("Customer or Employee? (c/e): ")
        print("\nDATA ENTRY")
        fname=input("First name: ")
        lname=input("Last name: ")
        emailAdress=input("Email: ")
        
        p = None
        if(option=='c'):
            number=input("Number: ")
            p=Customer(fname,lname,emailAdress,number)
        elif(option=='e'):
            ssn=input("SSN: ")
            p=Employee(fname,lname,emailAdress,ssn)

        if (p is not None):
            if (isinstance(p, Customer)):
                print("\nCUSTOMER")
                print("First Name: ",p.firstName())
                print("Last Name: ",p.lastName())
                print("Email: ",p.emailAdress())
                print("Number: ",p.customerNumber())
            elif (isinstance(p, Employee)):
                print("\nEmployee")
                print("First Name: ",p.firstName())
                print("Last Name: ",p.lastName())
                print("Email: ",p.emailAdress())
                print("SSN: ",p.socialNumber())

        cont=input("\nContinue? (y/n): ")
        if(cont=='y'):
            print()
            continue
        if(cont=='n'):
            print ("\nBye!")
            break

if __name__ == '__main__':
    main()

