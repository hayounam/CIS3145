# Hayoung Nam
# June 28 2020
# Monthly Sales & Yearly Sales check program
# Create a program that reads sales for 12 months and calculates the total yearly sales.
# User can edit the sales for any month.
# User can input string method for sales amount

import os
global month_name

def load_file(filename):
    try:
        dictionary={}
        with open(filename,'r') as infile:
            next(infile) # skip header
            for line in infile.readlines():
                line = line.strip().split(',')
                try:
                    dictionary[line[0].lower()] = line[1].strip()
                except:
                    continue

    except FileNotFoundError:
        print("ERROR - Unable to open {}".format(filename))
        quit()

    return dictionary

def monthlySales(dictionary):
    month_ns=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    for month in month_ns:
        sales = dictionary.get(month.lower())
        if (sales == 'TK'):
            print("{0} - 뀨?  {1:>8}".format(month, sales))
        else:
            print("{0} - {1:>8}".format(month, round(float(sales))))

def yearlySales(dictionary):
    total = 0
    for sales in dictionary.values():
        if (sales == "TK"):
            sales = 0
            print ("Using sales amount of 0 for {}.".format(month_name))
        else:
            sales = float(sales)
        total+=sales
    average = total/len(dictionary)
    print("Yearly Total: {0}".format(round (total)))
    print("Monthly average: {0}".format(round(average,2)))

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def edit(dictionary,filename):
    global month_name
    month_ns=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    month_name=input("Three-letter Month: ").lower()
    if month_name in month_ns:
        sales_amount=input("Sales amount: ")
        if (sales_amount == 'TK' or is_float(sales_amount)):
            dictionary[month_name]=sales_amount
            update_file(dictionary,filename)
        else:
            print("ERROR - Invalid sales amount entered.")
    else:
        print("ERROR - Invalid month name entered.")

def update_file(dictionary, filename):
    try:
        with open(filename,'w') as outfile:
        #################################
            outfile.write("Month,Sales \n")
        ##################################
            print ()
            month_ns=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
            for month in month_ns:
                outfile.write("{0},{1}\n".format(month.title(),dictionary.get(month)))
            print("Sales amount of", month_name, "was modified.")

    except FileNotFoundError:
        print("ERROR - Unable to open {}".format(filename))
        quit()

def main():
    filename="monthly_sales.csv"
    dictionary = load_file(filename)
    print("Monthly Sales program")
    while True:
        print()
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
