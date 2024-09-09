year= int(input("Enter a year: "))
if year%100==0:
    if year%400==0:
        print("This is a leap year.")
    elif year%400!=0:
        print("This is not a leap year")
elif year%100 !=0 and year%4==0:
        print("This is a leap year.")
else:
    print("This is not a leap year.")

