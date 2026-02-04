
is_prime = True

input_no = int(input("Enter Your no: "))
if input_no > 1:
    for i in range(2, input_no):
         if (input_no % i) == 0:
              is_prime = False
              break
        

if is_prime:
     print("Prime no", input_no)
else:
     print("Not Prime")             

