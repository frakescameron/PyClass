name = input("Enter your full name: ")

# result = len(name)
result = name.find(" ")
result = name.find("B")
result = name.find("o")
result = name.rfind("o")
result = name.rfind(" ")
name = name.capitalize()
name = name.upper()
name = name.lower()
result = name.isdigit()
result = name.isalpha() 
# will return -1 with no results


print(name)