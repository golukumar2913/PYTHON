# Find Lcm and print

a = int(input("Enter no "))
b = int(input("Enter second no "))

x , y = a , b

# find gcd
while y != 0:
    x , y = y , x % y

gcd = x


lcm = (a * b) // gcd
print("LCM = ",lcm)

