pattern = "*"
n = 6

for i in range(n, 0, -1):
    for j in range(i):
        print(pattern, end="")
    print()    

