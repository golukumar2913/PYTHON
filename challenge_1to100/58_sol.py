# Count Vowel

s = input("Enter String ")

count = 0
          
for i in range(len(s)):
    if s[i] in "aeiouAEIOU":
        count += 1

print("Total vowels:", count)

    


