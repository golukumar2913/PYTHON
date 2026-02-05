final_result = 1
even_counter = 0
odd_counter = 0
neg_counter = 0

while True:
    input_no = int(input("Enter Your No: "))

    if input_no == -1:
        break

    if input_no == 0:
        continue
    

   
    if input_no < 0:
        if neg_counter < 2:
            final_result *= input_no
            neg_counter += 1


    elif input_no % 2 == 0:
        if even_counter < 4:
            final_result += input_no
            even_counter += 1

    
    else:
        if odd_counter < 3:
            final_result -= input_no
            odd_counter += 1

print(final_result)