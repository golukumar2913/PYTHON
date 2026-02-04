numbers = [5, 8, 3, 12, 7, 4, 10, 1, 6]

counter = 0
total = 0

for num in numbers:
    if num % 2 == 0 :
        counter += 1
        if counter <= 2 :
            total += num
        elif counter <= 4:
            total -= num
        else:
            break 


print(total)           
             
        

