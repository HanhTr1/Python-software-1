smallest = None
largest = None

while True:
    num = input("Enter a number: ")
    if num == "":
        break
    try:
        convert = float(num)
        if smallest is None or convert < smallest :
            smallest = convert
        if largest is None or convert > largest :
            largest = convert
    except ValueError:
        continue

if smallest is not None and largest is not None:
    print(f"The smallest number is: {smallest}")
    print(f"The largest number is: {largest}")




