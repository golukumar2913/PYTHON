sum_input = 0



while True:
    input_no = int(input("Enter Your No: "))
    if  input_no == 0 :
        break
    elif input_no % 2 != 0:
         continue
    else:
        sum_input += input_no
          

print (sum_input)  