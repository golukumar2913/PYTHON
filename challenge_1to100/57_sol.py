# String Palindrome check

s = input("Enter String ")

temp = s 
reverse = ""
for i in s:
    reverse = i + reverse

if reverse == temp:
    print("Palindrome")
else:
    print("Not Palindrome")    