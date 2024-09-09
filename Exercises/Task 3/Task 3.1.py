zander_length = float(input("Enter the length of a zander in centimeters:"))
limit=42
if zander_length<limit:
    print(f"The zander is shorter {limit-zander_length} cm than the limit.")
    print("Please release it back to the lake!")
else:
    print("You can take the zander!")



