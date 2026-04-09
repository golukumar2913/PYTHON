# Replace Character 

s = input("Enter string ")

old = input("Enter character to replace ")
new = input("Enter new ")

result = ""

for c in s :
    if c == old:
        result += new 
    else:
        result += c 

print(result)             