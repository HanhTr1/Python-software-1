talents=float(input("Enter the number of talents: "))
pounds=float(input("Enter the number of pounds: "))
lots= float(input("Enter the number of lots: "))

weight= 13.3*lots+13.3*32*pounds+13.3*32*20*talents
in_kilogram=int(weight/1000)
in_grams=weight-in_kilogram*1000
print(f"The weight in modern units:\n{in_kilogram} kilograms and {in_grams:.2f} grams.")
