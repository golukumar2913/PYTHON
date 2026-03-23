# Print odd no for num

num = int(input("Enter No "))

if num == 0:
    print("Odd no Find not possible")
elif num == 1 :
    print(f"Only one odd no {1}") 
else: 
    count = 0
    for i in range (1, num + 1)  :
        if i % 2 != 0:
            print(i)
            count += 1
     
    print(f"Total odd no {count}")