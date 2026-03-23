# factorial

num = int(input("Enter No "))

factorial = 1

if num < 0 :
    print("Factorial not possible")
elif num == 0 or num == 1:
    print(factorial) 
else:
    for i in range(1, num+1):
       factorial *= i
    print(factorial)
