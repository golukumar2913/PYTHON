S = input("Enter Word ")

count = 0

for i in range(len(S)):
    if S[i] in "aeiouAEIOU":
        count
    else:
        count+= 1

print(f"Consonent = {count}")