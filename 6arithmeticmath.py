#friends = 5

# friends = friends + 1
# friends += 1
# friends = friends - 2
# friends -= 2
# friends = friends * 3
# friends *= 3
# friends = friends / 2
# friends /= 2
# friends = friends ** 2
# friends **= 2
# remainder = friends % 3


# print(remainder)

# x = 3.14
# y = -4
# z = 5

# result = round(x)
# result = abs(y)
# result = pow(4, 2)
# result =max(x , y, z)
# result = min(x , y, z)

# print(result)

# import math


# x = 9.9

# print(math.pi)
# print(math.e)
# result = math.sqrt(x)
# result = math.ceil(x)
# result = math.floor(x)

# print(result)


### radius calculator problem
# import math

# r = float(input("What is the radius of the circle? :"))
# pi = (math.pi)
# c = 2 * pi * r

# print(f"The circumfrence of the circle is :{round(c, 4)}cm")

### area calculator problem
# import math

# radius = float(input("What is the radius of the circle? :"))
# area = math.pi * pow(radius, 2)
# print(f"The area of the circle is {round(area, 4)}cm")

### pythagorien therum

import math

a = float(input("What is the a of the triangle? :"))
b = float(input("What is the b of the triangle? :"))

mathy = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The c value of the triangle is {round(mathy, 4)} ")