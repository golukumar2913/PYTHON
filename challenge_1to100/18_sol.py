# count Digit

num = int(input("Enter Only  No "))
Name = input("Enter number: ")
digit = abs(num)
count = 0
 
if digit == 0:
    count += 1
else:
    while digit > 0:
        digit //= 10
        count += 1

print("Total digits =", count)       
print("Total digits =", len(Name))
  