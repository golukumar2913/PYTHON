# Find index of element
arr = list(map(int, input("Enter list value ").split()))
no = int(input("Enter no find index "))

for i in range(len(arr)):
    if arr[i] == no:
       print(i)