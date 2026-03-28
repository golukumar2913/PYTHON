# check perfect no 

num = int(input("Enter no "))

total = 0 

for i in range(1, num):
    if num % i == 0:
        total += i

print(total)
if total == num:
    print("Perfect Number")
else:
    print("Not Perfect Number")       