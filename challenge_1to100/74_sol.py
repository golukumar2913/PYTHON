# 2nd largest number

lis = list(map(int, input("Enter no ").split()))

largest = sec = float('-inf')

for num in lis :
    if num > largest :
        sec = largest
        largest = num 
    elif num > sec and num != largest:
        sec = num

print(f"2nd largest no = {sec}")
        