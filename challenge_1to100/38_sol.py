# Count digits in number

num = int(input("Enter no "))
nums = abs(num)
count = 0

if nums == 0:
    count += 1
else:
    while nums > 0:
        nums //= 10
        count += 1

print("count ",count)        