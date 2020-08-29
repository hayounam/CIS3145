# Hayoung Nam
# Arrival Time Estimator
# July 5 2020
# Create a program that calculates the estimated duration of a trip

import datetime
from datetime import timedelta

print("Arrival Time Estimator\n")

cont = "y"

while (cont == "y"):
    date = input("Estimated date of departure (YYYY-MM-DD) : ")
    dept_dt = datetime.datetime.strptime(date,"%Y-%m-%d")

    miles = input("Enter miles : ")
    try:
        miles = int(miles)
        if miles <= 0:
            print ("Enter a number greater than 0. \n")
            miles = input("Enter miles : ")
        
    except ValueError:
        print ("Format Error. Try Again")
        miles = input("Enter miles : ")

    
    speed = input("Enter miles per hour : ")
    try:
        speed = int(speed)
        if speed <= 0:
            print ("Enter a number greater than 0. \n")
            speed = input("Enter miles per hour : ")
        
    except ValueError:
        print ("Format Error. Try Again")
        speed = input("Enter miles per hour : ")

    
    print("\nEstimated travel time ")
    hours = miles//speed
    minutes = round((miles%speed))
    print("Hours: ", hours)
    print("Minutes: ", minutes)

    ar_dt = dept_dt + timedelta(hours=hours,minutes=minutes)
    ar_date = ar_dt.strftime("%Y-%m-%d")
    ar_time = ar_dt.strftime("%I:%M %p")
    print("Estimated date of arrival : ", ar_date)
    print("Estimated time of arrival : ", ar_time)

    
    cont = input("\nContinue? (y/n): ")

print("\nBye!")
