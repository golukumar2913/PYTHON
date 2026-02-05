
total = 1
divide_five_counter = 0
divide_three_counter = 0
neg_counter = 0

while True :
    number = int(input("Enter your no: "))

    if number == 999 :
        break

    if number == 0 and (number % 3 == 0 and number % 5 == 0):
        continue

    if number < 0:
        if neg_counter < 2:
            total *= number
            neg_counter += 1       
    elif number % 5 == 0:
        if divide_five_counter < 3:
            total += number
            divide_five_counter += 1
    else:
        if number % 3 == 0:
            if divide_three_counter < 4:
                total -= number
                divide_three_counter +=1 


print("Final Result", total)                