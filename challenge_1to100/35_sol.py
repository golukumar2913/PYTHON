# product of digits

num = int(input("Enter no "))

product = 1

while num > 0:
    digit = num % 10
    product *= digit
    num //= 10

print("Product of digits =", product)    
