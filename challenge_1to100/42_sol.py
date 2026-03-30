# Reverse star tringle 

n = int(input("Enter no "))

for i in range(n, 0 , -1):
    for i in range(i):
        print("*", end=" ")
    print()    