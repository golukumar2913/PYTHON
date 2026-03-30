n = int(input("Enter no"))

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2*i - 1))

# Lower Pyramid
for j in range(1, n):
    print(" " * j, end="")
    print("*" * (2*(n - j) - 1))