# Hayoung Nam
# June 24 2020
# Monthly Sales & Yearly Sales check program
# Create a program that reads sales for 12 months and calculates the total yearly sales.
# User can edit the sales for any month.

import os

def load_file(filename):
    if os.path.isfile(filename) is not True:return None

    dictionary={}
    with open(filename,'r') as infile:
        for line in infile.readlines():
            line = line.strip().split(',')
            try:
                dictionary[line[0].lower()] = float(line[1].strip())
            except:
                continue

    return dictionary


def monthlySales(dictionary):
    month_ns=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    for month in month_ns:
        print("{0} - {1:>8}".format(month, round(dictionary.get(month.lower()))))


def yearlySales(dictionary):

    total =0
    for sales in dictionary.values():
        total+=sales
    average = total/12
    print("Yearly Total: {0}".format(round (total, 2)))
    print("Monthly average: {0}".format(round(average,2)))

def edit(dictionary,filename):
    month_ns=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    month_name=input("Three-letter Month: ").lower()
    if month_name in month_ns:
        sales_amount=float(input("Sales amount: "))
        for month,sales in dictionary.items():
            if month==month_name:
                dictionary[month_name]=sales_amount
                update_file(dictionary,filename)
    else:
        print("ERROR - Invalid month name entered.")


def update_file(dictionary, filename):
    with open(filename,'w') as outfile:
        #################################
        outfile.write("Month,Sales \n")
        ##################################
        print ()
        month_ns=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
        for month in month_ns:
            outfile.write("{0},{1}\n".format(month.title(),dictionary.get(month)))
        print("Sales amount of {} was modified.".format(filename))

def main():

    filename="monthly_sales.csv"
    dictionary = load_file(filename)
    if dictionary is None:
        print("ERROR - Unable to open {}".format(filename))
        return
        ##########################################
    while True:
        
        print()
        print("Monthly Sales program \n")
        print("monthly - View monthly sales")
        print("yearly	- View yearly summary")
        print("edit	- Edit sales for a month ")
        print("exit	- Exit program")
        print()
        ###########################################
        choice=input("Command: ")
        if choice == "monthly":
            monthlySales(dictionary)
        elif choice =="yearly":
            yearlySales(dictionary)
        elif choice =="edit":
            edit(dictionary,filename)
        elif choice=="exit":
            print ("Bye!")
            break
        else:print("ERROR - Invalid")
        
if __name__ == "__main__":
    main()
