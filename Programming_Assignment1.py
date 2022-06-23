# '1. Write a Python program to print 'Hello Python'?

print("Hello Python")
print()

# 2. Write a Python program to do arithmetical operations addition and division.?

a = 5
b = 7

c = a + b

print("Addition of", a, ',', b, " is", c)
d = b - a

print("Substraction of", a, ',', b, " is", d)

print()
# 3. Write a Python program to find the area of a triangle?


a = 2
b = 3
c = 4

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('The area of the triangle is %0.2f' % area)
print()
# 4. Write a Python program to swap two variables?
a = 2
b = 4
print('Before  swap a=', a, "b=", b)
a, b = b, a

print("After swap a=", a, 'b=', b)

print()
# 5. Write a Python program to generate a random number?

import random

print(random.randint(0,50))
