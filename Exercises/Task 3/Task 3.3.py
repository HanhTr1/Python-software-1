gender = input("Enter your biological gender: ")
hemoglobin_value = float(input("Enter your hemoglobin value: "))
if gender == "Male":
    if 134<= hemoglobin_value <= 167:
        print("Hemoglobin is normal")
    elif hemoglobin_value< 134:
        print("Hemoglobin is low")
    elif hemoglobin_value> 167:
        print("Hemoglobin is high")
elif gender == "Female":
    if 117<= hemoglobin_value <= 155:
        print("Hemoglobin is normal")
    elif hemoglobin_value< 117:
        print("Hemoglobin is low")
    elif hemoglobin_value> 155:
        print("Hemoglobin is high")


