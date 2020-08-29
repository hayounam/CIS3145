# Hayoung Nam
# June 21 2020
# Quarterly Sales
# Create a program that gets quarterly sales from a user and calculates the total of all four quarters as well as the average, lowest, and highest quarters.

print ("The Quarterly Sales program")
print()

q1 = float(input ("Enter Sales for Q1 : "))
q2 = float(input ("Enter Sales for Q2 : "))
q3 = float(input ("Enter Sales for Q3 : "))
q4 = float(input ("Enter Sales for Q4 : "))
salesLists = [q1, q2, q3, q4]
    

    
totalsum = 0
for i in salesLists:
    totalsum += i
        
avg = sum(salesLists,0) / len(salesLists)
low = min(salesLists)
high = max(salesLists)

   

print()
print ("Total:" , round (totalsum, 2))
print ("Average Quarter:", round (avg, 2))
print ("Lowest Quarter:", round (low, 2))
print ("Highest Quarter:", round (high, 2))
