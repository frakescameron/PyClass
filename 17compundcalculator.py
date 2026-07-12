balance = 0

interest = 0

years = 0

while balance <= 0:
    balance = float(input("What is your initial balance?: "))
    if balance <= 0:
        print("Balance cannot be less than or equal to 0")

while interest <= 0:
    interest = float(input("What is the interest rate?: ")) 
    if interest <= 0:
        print("interest cannot be less than or equal to 0")

while years <= 0:
    years = int(input("How many years will it compound?: ")) 
    if interest <= 0:
        print("years cannot be less than or equal to 0")

total = balance * pow((1 + interest / 100), years)

print(f"Balance after {years} year/s: ${total:.2f}")