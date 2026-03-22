# Reverse No

num = int(input("Enter no "))

num = abs(num)
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print(reverse)
