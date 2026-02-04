
final_total = 1
divide_five_count = 0
divide_three_count = 0
neg_count = 0

while True :
    number = int(input("Enter Your no"))

    if number == 999 :
        break
    
    if number == 0:
        continue

    if number % 3 == 0 and number % 5 == 0:
        continue

    if number < 0:
        if neg_count < 2:
            final_total *= number
            neg_count += 1       
    elif number % 5 == 0:
        if divide_five_count < 3:
            final_total += number
            divide_five_count += 1
    else:
        if number % 3 == 0:
            if divide_three_count < 4:
                final_total -= number
                divide_three_count +=1        




