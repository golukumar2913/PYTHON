s = input("Enter Sentence ")

count = 0

for i in range(len(s)):
    if s[i] == " ":
        count += 1

print(f"Total Word = {count + 1}")

# better method 

words = s.split()
new_count = 0

for word in words:
    new_count += 1
print(f"Total Word = {new_count}")

