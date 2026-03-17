# check Leap Year

No = int(input("Enter Year "))

if No % 4 == 0  and No % 100 != 0 :
    print("Leap Year ", No)
elif No % 400 == 0:
    print("Leap Year ", No)
else :
    print("Not Leap year", No)    