# Merge Two list

arr1 = list(map(int, input("Enter first list ").split()))
arr2 = list(map(int, input("Enter 2nd list ").split()))


i = 0
j = 0
mergelist = []

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        mergelist.append(arr1[i])
        i += 1
    else:
        mergelist.append(arr2[j])
        j += 1

while i < len(arr1):
    mergelist.append(arr1[i])
    i += 1
    
while j < len(arr2):
    mergelist.append(arr2[j])  
    j += 1
  
print(mergelist)


