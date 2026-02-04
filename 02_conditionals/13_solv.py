number = -77

# abs() se positive + negative ek saath handle hote hain

if 10 <= abs(number) <= 99:
    if number % 2 == 0:
        print("Two-digit Even")
    else :
        print ("Two-digit Odd")
# elif -99 <= number <= -10 :
#     if number %2 == 0:
#         print(" - Two digit Even")
#     else :
#         print ("- Two-digit Odd")    
else:
    print("Not a two-digit number")

