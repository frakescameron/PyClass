unit = input("Is the temp in Celcius or Fahrenheit? (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheight is {temp}F")
elif unit == "L":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celcius is {temp}C")
else: 
    print(f"{unit} was not valid")
