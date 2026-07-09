operator = input("enter an operator (+ - * /): ")
numb1 = float(input("What is your first number?: "))
numb2 = float(input("What is your second number?: "))

if operator == "+":
    print(f"The answer is {numb1 + numb2}")
elif operator == "-":
    print(f"The answer is {numb1 - numb2}")
elif operator == "*":
    print(f"The answer is {numb1 * numb2}")
elif operator == "/":
    print(f"The answer is {numb1 / numb2}")
else:
    print("Please enter a suitable number")