# check largest no and Minimum no

a = int(input("Enter A  "))
b = int(input("Enter B  "))
c = int(input("Enter C  "))
d = int(input("Enter D  "))

if a >= b and a >= c and a >= d:
    print("Largest =", a)
elif b >= a and b >= c and b >= d:
    print("Largest =", b)
elif c >= a and c >= b and c >= d:
    print("Largest =", c)
else:
    print("Largest =", d)



# use Built-in function
print("Using Built In")
largest = max(a , b, c, d)
print("largest No ", largest )

minimum = min(a , b , c, d)
print("Minimum No ", minimum )