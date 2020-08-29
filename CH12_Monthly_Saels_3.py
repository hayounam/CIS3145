import os

FILENAME = open("monthly_sales.txt", "r+")         
dictionary = {}                                    

for line in FILENAME.readlines():                  
    data = line.strip().split()                    
    month = data[0].strip()                      
    sale = float(data[1].strip())                  
    dictionary[month] = sale                        

FILENAME.close()                                  

print("Monthly Sales Program")

while True:
    print("\nCOMMAND MENU")
    print("view - View sales for specified month")
    print("edit - Edit sales for specified month")
    print("totals - View sales summary for year")
    print("exit - Exit Program\n")
    
    choice = input("Command: ")                
    choice = choice.lower()

    if choice == "view":                       
        month = input("Three-letter Month: ")   
        found = False                           
        for option in dictionary.keys():           
            if month.lower() == option.lower():    
                print("Sales amount for", option, "is {:,.2f}".format(dictionary[option]))
                found = True                   
                break
        if not found:                           
            print("Invalid three-letter month")

    elif choice == "edit":                     
        month = input("Three-letter Month: ")
        found = False
        for option in dictionary.keys():
            if month.lower() == option.lower():    
                sales_amount = float(input("Sales Amount: "))
                dictionary[option] = sales_amount  
                print("\nSales amount for", option, "is {:,.2f}".format(dictionary[option]))
                found = True
                break
        if not found:                           
            print("Invalid three-letter Month")
    elif choice == "totals":                   
        total_sales = 0
        for option in dictionary.keys():           
            total_sales += dictionary[option]      
        monthly_average = total_sales / len(dictionary)      
        print("Yearly total: {:,.2f}".format(total_sales))
        print("Monthly Average: {:,.2f}".format(monthly_average))

    elif choice == "exit":                     
        print('\nBye!')
        
        # new dictionary file import
        with open("monthly_sales.txt","w") as FILENAME:
            for mon, sale in dictionary.items(): # dictionary key=mon , value=sale
                FILENAME.write(mon)
                FILENAME.write("\t") 
                FILENAME.write(str(int(sale)))
                FILENAME.write("\n")
            FILENAME.close()
        exit(0)

    else:                                       
        print("ERROR - Invalid command")
