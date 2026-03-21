# check Tringle validation using Angles

A = int(input("Enter A angle = "))
B = int(input("Enter B angle = "))
C = int(input("Enter C angle = "))

if A + B + C == 180 and A > 0 and B > 0 and C > 0:
    print("Triangle Valid")
else:
    print("Not Valid")