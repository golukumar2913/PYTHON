# Reverse List 

arr = list(map(int, input("Enter numbers: ").split()))

rev = []

for i in range(len(arr)-1, -1, -1):
    rev.append(arr[i])

print("Reversed list:", rev)


# slice method 
lis_rev = arr[::-1]
print("Reversed list:", lis_rev)
 
# short method built in 
arr.reverse()
print("Reversed list:", arr)



