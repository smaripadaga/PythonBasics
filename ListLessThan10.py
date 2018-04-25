NumberElement = int(input("Enter how many numbers in the list")) #number of elements in the list
NumberElementList = range(0,NumberElement)
list = []
for num in NumberElementList:
    temp = int(input("Enter actual number"))
    list.append(temp)
#get every element and check if less than 10
for num2 in list:
    if num2 < 10:
        print(num2)





