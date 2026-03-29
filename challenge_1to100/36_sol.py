a = int(input("Enter no "))
b = int(input("Enter second no "))

while b != 0:
    a , b = b, a % b 

print("GCD =",a)    