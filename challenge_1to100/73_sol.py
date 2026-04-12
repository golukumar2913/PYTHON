# Smallest no

lis = list(map(int, input("Enter no ").split()))

smallest = lis[0]

for i in lis :
    if i < smallest:
        smallest = i

print("smallest" , smallest) 

# short method 
print(f"Smallest = {min(lis)}")