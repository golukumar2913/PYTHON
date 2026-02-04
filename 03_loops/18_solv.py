
final_result = 0
odd_counter = 0
even_counter = 0

while True:
    numbers = int(input("Enter Your No: "))
    if numbers == 0:
        break
    if numbers % 2 == 0:
        if even_counter < 3:
            final_result += numbers
            even_counter += 1 
        else:
            continue
    else:
        if odd_counter < 2 :
            final_result -= numbers
            odd_counter += 1
        else :
            continue    

print(final_result)

# Total = 0
# even_count = 0
# odd_count = 0

# while True:
#     input_no = int(input("Enter Your No: "))
    
#     if input_no == 0:
#         break

#     if input_no % 2 == 0:
#         if even_count < 3:
#             Total += input_no
#             even_count += 1
#     else:
#         if odd_count < 2:
#             Total -= input_no
#             odd_count += 1

# print(Total)
