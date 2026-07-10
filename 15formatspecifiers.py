# format specifiers = {value:flags} format a value based on the flags inserted

price1 = 3000.12564956829198149
price2 = -9808.22
price3 = 1002.34

print(f"price 1 is {price1:.1f}")
print(f"price 2 is {price2:10}")
print(f"price 3 is {price3:010}")
print(f"price 3 is {price3:>10}")
print(f"price 3 is {price3:<10}")
print(f"price 3 is {price3:^10}")
print(f"price 3 is {price3:+}")
print(f"price 3 is {price3: }")
print(f"price 3 is {price3:,.2f}")
print(f"price 3 is {price3:+,.2f}")
