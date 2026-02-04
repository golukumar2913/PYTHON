import math

def circle_stats(radius):
    area = math.pi * radius **2
    circumference = 2 * math.pi * radius
    return area, circumference


area , circum = circle_stats(4)

# convert long float to short
a = f"{area:.3f}"
y = f"{circum:.3f}"

print("Area: ", a, "Circumference: ", y)