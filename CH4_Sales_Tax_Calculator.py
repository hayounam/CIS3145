# Hayoung Nam
# CH4 Sales Tax Calculator
# June 18 2020
# Create a program that uses a seperate module to calculates sales tax and total after tax


print ("Sales Tax Calculator")

def getItems ():

    print ()

    print ("ENTER ITEMS (ENTER 0 TO END)")

    print ()

    total = 0

    while True:

        cost = float (input ("Cost of item: "))

        if cost == 0:

            break

        total += cost

    return total


def calculations (total):

    """

    Calculates sales tax


    """

    rate = 6

    salesTax = (rate/100) * total

    totalwithTax = salesTax + total

    return salesTax, totalwithTax




def printResult(total):

    salesTax, totalwithTax = calculations (total)

    total = round (total, 2)

    salesTax = round (salesTax, 2)

    totalwithTax = round (totalwithTax, 2)



    print ("Total:\t", total)

    print ("Sales Tax: ", salesTax)

    print ("Total after tax: ", totalwithTax)



def main ():

    choice = "y"

    while choice.lower() == "y":

        total = getItems ()

        printResult(total)

        

        print()

        choice = input ("Again? (y/n) :")



    print ()

    print ("Thanks, bye!")



if __name__ == "__main__":

    main()


 
