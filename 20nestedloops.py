# a nested loop = a loop within another loop (outer, inner)

rows = int(input("enter the number of rows: "))
columns = int(input("Enter the number of colums: "))
symbol = input("Enter a symbol to use")

for x in range(rows):
    for y in range (columns):
        print(symbol, end = " ")
    print()
