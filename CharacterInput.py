import datetime
name = str(input("Enter your name"))
age = int(input("Enter your age"))
currentyear = int(datetime.date.today().strftime("%Y"))
futureyear = (currentyear) + 100 - (age)
print("\nHello " + name + " will turn 100 years in " + str(futureyear))