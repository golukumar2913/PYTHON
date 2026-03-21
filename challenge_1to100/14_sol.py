# check Tringle validation using side

A = int(input("Enter A side = "))
B = int(input("Enter B side = "))
C = int(input("Enter c side = "))

is_valid = True

if A > 0 and B > 0 and C > 0 and (A + B > C and A + C > B and B + C > A) :
    is_valid = True
else:
    is_valid = False


if is_valid :
    print("Tringle Valid")
else:
    print("Not Valid ")

