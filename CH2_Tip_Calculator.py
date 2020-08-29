# Hayoung Nam 
# CH2 Tip calculator
# June 10 2020 
# Create a tip calculator program that calculates the tip and total cost for meal at a restaurant

# Title
print ("Tip calculator\n")

# Input 

cost_of_meal = float (input ("Enter meal cost: \t"))
tip_percent = float (input ("Enter tip cost: \t"))

#Calculation

tip = cost_of_meal * (tip_percent / 100)
total = tip + cost_of_meal
tip = round (tip, 2)
total = round (total, 2)

#Print

print ()
print ("Tip amount : \t" + str (tip))
print("Total amount : \t" + str (total))
print ()

# Exit option
while True:
    n = input ("If you are done, press enter: \n")
    if n == '':
        break;
