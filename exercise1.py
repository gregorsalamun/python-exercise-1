from datetime import datetime
now = datetime.now()

name = input("What is your name? " + "\n")
age = int(input("How old are you? " + "\n"))
year = str((now.year - age)+100)

print("You will be 100 years old in the year " + year + "\n")
nyear = ("You will be 100 years old in the year " + year + "\n")  

repeat = int(input("Input number and be suprised :) "))

print (nyear * repeat) 
