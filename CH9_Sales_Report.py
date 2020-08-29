# Hayoung Nam
# Sales Report
# July 2 2020
# Create a program that displays a report of sales by quarter.

import locale
lc.setlocale(lc.LC_All, "us")

sales = [[1540.0, 2010.0, 2450.0, 1845.0],
         [1130.0, 1168.0, 1847.0, 1491.0],
         [1580.0, 2305.0, 2710.0, 1284.0],
         [1105.0, 4102.0, 2391.0, 1576.0]]

print("Sales Report\n")
print("{:10s} {:10s} {:10s} {:10s} {:10s}".format("Region","Q1","Q2","Q3","Q4"))

numbering=1
for region in sales:
    print("{:4s} ".format(str(numbering)),end='')
    for i in region:
        print("{:10,.2f} ".format(i),end="")
    print()
    numbering +=1

print("\nTotal Sales by region:")
numbering = 1
total_sales=0
for region in sales:
    sum=0 
    for i in region: 
        sum += i
    total_sales += sum 
    print("Region "+ str(numbering)+": ${:4,.2f}".format(sum))
    numbering += 1

print("\nTotal Sales by quarter:")
quarter = [0,0,0,0] 
for f in sales:
    quarter[0] += f[0]
    quarter[1] += f[1]
    quarter[2] += f[2]
    quarter[3] += f[3]

f=1
for i in quarter:
    print("Q"+str(f)+": ${:4,.2f}".format(i))
    f+=1

print("\nTotal annual sales, all regions: ${:,.2f}".format(round(total_sales)))
