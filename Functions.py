# hours, rate and minimum hour condition
hours = float(input("Enter number of hours worked:"))
rate = float(input("Enter rate per hour:"))
minhrs = float(40)
extrarate = (rate * 0.5) + rate
extrahrs = hours - minhrs


# define computepay
def computepay():
    print(a + b)
    return


# our conditions
if hours > minhrs:
    a = minhrs * rate
    b = extrahrs * extrarate
else:
    print("did not meet minimum")

computepay()

