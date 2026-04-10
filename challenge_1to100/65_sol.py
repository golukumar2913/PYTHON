# Remove duplicte from string

s = input("Enter string ")

result = ""

for i in s :
    if i not in result :
        result += i
print(result)        

