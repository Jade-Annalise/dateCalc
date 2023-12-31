# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 20:43:19 2023

@author: jade annalise 
"""
#jade annalise
#date difference calulcator 
#takes two dates from the user and calculates amount of days between 

import datetime #imports datetime module

#explains how the calculator works to the user
#including showing the format for the input so that the list indexes are correct
print("Welcome to the date difference calculator! Provide me with two dates and I'll calculate the time between them.")
print("Please make sure to write the date in the year, month, day format. \nFor example:\n2023/08/14")

#takes the input of the two dates and stores them to two variables, A stores the first, B stores the second 
dateAStore = input("\nWhat is the first date? ")
dateBStore = input("What is the second date? ") 

#converts the input into two lists to parse into the date classes, splitting the strings at the / sign 
listDateA = dateAStore.split("/")
listDateB = dateBStore.split("/")

#creates the datetime classes for each date, with list indexes aligned for the 
dateA = datetime.date(int(listDateA[0]), int(listDateA[1]), int(listDateA[2]))
dateB = datetime.date(int(listDateB[0]), int(listDateB[1]), int(listDateB[2])) 

#calculates the difference between the two dates
dayNo = (dateA - dateB)

#converts dayNo variable into a string
#removes negative sign if present, also removes extra comma and time information
finalDay = str(dayNo).replace("-","").replace(",", "").replace("0:00:00","") 

#prints the finalDay variable with some extra text
print("\nThe number of days between " + dateAStore + " and " + dateBStore + " is " + finalDay)
 

