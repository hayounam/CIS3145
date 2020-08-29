# Hayoung Nam 
# CH3 Tip calculator
# June 13 2020 
# Create a tip calculator program that calculates three options for tip and total cost for meal at a restaurant


print("Tip Calculator \n")

cost = float(input("Cost of meal: "))
print()

for tip in range(15,26,5):
    print("%d%% \nTip amount: %.2f \nTotal amount: %.2f\n"%(tip,cost*tip/100,cost*(tip+100)/100))
