numbers = [3, 6, 2, 9, 12, 15, 8, 7, 4]

total = 0
count_even = 0

for i in numbers :
    if i % 2 == 0 :
        total += i
        count_even +=1
        if count_even == 3:
          break


print(total)