# print sum 1 to n

N = int(input("Enter your No "))

sum1 = 0 
sum_w = 0
for i in range( 1 , N+1):
    sum1 += i

i = 1
while i <= N:
    sum_w +=i
    i+=1

print(sum1) 
print(sum_w)   