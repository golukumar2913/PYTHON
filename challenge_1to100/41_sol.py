# Star triangle Pattern print 

n = int(input("Enter no for star printing "))

for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print()    