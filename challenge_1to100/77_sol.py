# Count occurrences

arr = list(map(int, input("Enter no ").split()))

freq = {}

for i in arr :
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(f"Count occurrences {freq}")