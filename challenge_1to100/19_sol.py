num = int(input("Enter Only  No "))

digit = abs(num)
num_sum = 0
 
if digit == 0:
    num_sum += 1
else:
    while digit > 0:
        last = digit % 10
        num_sum += last
        digit //= 10
        

print("Total digits Sum =", num_sum)       
