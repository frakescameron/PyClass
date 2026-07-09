# logical does or, and, not

# temp = 25
# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")


temp = 28
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is Hot ouside")
    print("It is SUNNY")
elif temp <= 0 and is_sunny:
    print("It is cold and it is sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is warm and sunny")
elif 28 > temp > 0 and not is_sunny:
    print("It is warm and not sunny")
elif temp <= 0 and not is_sunny:
    print("It is cold and it is not sunny")


