hrs = input("Enter Hours:")
h = float(hrs)
minhrs = float(40)
rate = input("Enter hourly rate:")
r = float(rate)
if h > minhrs:
    extrahrs = h - minhrs
    extrarate = r * 1.5
    grosspay = (minhrs * r) + (extrahrs * extrarate)
    print(grosspay)
else:
	print("Minimum hours not met")