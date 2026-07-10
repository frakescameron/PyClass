# name = input("Enter your full name: ")
# phone_number = input("What is your phone number?: ")

# result = len(name)
# result = name.find(" ")
# result = name.find("B")
# result = name.find("o")
# result = name.rfind("o")
# result = name.rfind(" ")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha() 
# result = phone_number.count("-")
# will return -1 with no results
# phone_number = phone_number.replace("-" , "")

# print(phone_number)


username = input("Please enter a new username. It must be more than 12 characters, contain no spaces, and must not contain digits: ")

if len(username) > 12:
    print("Your username cannot be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username cannot contain any digits")
elif not username.isalpha():
    print("Your username cannot have any numbers")