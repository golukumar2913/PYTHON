# Find Lcm and print
a = int(input("Enter no "))
b = int(input("Enter second no "))

x , y = a , b

# find gcd
while y != 0:
    x , y = y , x % y

gcd = x
print(gcd)

lcm = (a * b) 
print("LCM = ",lcm)

