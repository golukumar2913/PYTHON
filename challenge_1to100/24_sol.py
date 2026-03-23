# Multiplication Table

num = int(input("Enter No "))

# i = 1

# while i <= 10:
#     table = i * num
#     print(num , "*", i ,"=" , table)
#     i += 1


for i in range (1, 11):
    table = num * i
    print(f"{num} * {i} = {table}")