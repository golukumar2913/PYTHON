# divisible check

no = int(input("Enter Your No "))

if no % 5 == 0 and no % 11 == 0:
    print("Number is divisible by 5 and 11")
elif no % 5 == 0:
    print("Number is Divisible only 5")   
elif no % 11 == 0:
    print("Number is Divisible only 11")      
else:
    print("Number is not divisible by 5 and 11")