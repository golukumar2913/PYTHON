# check Armstrong number

num = int(input("Enter no "))

temp = num 
digits = len(str(num))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10
print(total)
if num == total :
    print("Armstrong number")
else:
    print("Not Armstrong")       