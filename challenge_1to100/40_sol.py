# Decimal no to binary no 

num = int(input("Enter number: "))

binary = ""

while num > 0:
    rem = num % 2
    binary = str(rem) + binary
    num //= 2

print("Binary =", binary)

print(bin(5))