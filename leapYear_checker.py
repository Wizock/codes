year = int(input("enter a year to check :"))
if year%4:
    if year%4:
        if year%400:
            leapYear = True
            print("the year "+str(year)+" is a leap year")
        else:
            leapYear = False
            print("the year "+str(year)+" is not a leap year")
        leapYear = True
        print("the year "+str(year)+" is a leap year")
    else:
        leapYear = False
        print("the year " + str(year) + " is not a leap year")
    leapYear = True
    print("the year " + str(year) + " is a leap year")
else:
    leapYear = False
    print("the year " + str(year) + " is not a leap year")