numbers = [4, -1, 7, 0, -3, 8, 5]

total_positive = 0
total_negaitive = 0

for num in numbers :
    if num > 0 :
        total_positive += 1
  
    elif num < 0 :
        total_negaitive += 1
        
    else:
        print("zero")       

print(total_positive)
print(total_negaitive)