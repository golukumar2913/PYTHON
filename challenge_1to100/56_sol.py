#  String reverse

n = input("Enter String ")

reverse = ""
for i in n:
    reverse = i + reverse
print(reverse)

# short method 

two = n[::-1]
print(two)