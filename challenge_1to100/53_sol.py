# Hollow Pyramid

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    # spaces
    for j in range(1, n - i + 1):
        print(" ", end="")

    # stars
    for j in range(1, 2 * i):
        if i == 1 or i == n or j == 1 or j == (2 * i - 1):
            print("*", end="")
        else:
            print(" ", end="")
    
    print()