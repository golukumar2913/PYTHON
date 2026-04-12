# Largest Element 

lit = list(map(int, input("Enter no ").split()))

largest = lit[0]   

for i in lit:
    if i > largest:
        largest = i

print("Largest ", largest)

# Short method 

print("Largest ", max(lit))