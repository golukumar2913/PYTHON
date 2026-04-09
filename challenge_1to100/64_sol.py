# Most Frequent number 

arr = list(map(int, input("Enter no ").split()))

freq = {}
for i in arr :
    if i in freq:
        freq[i] += 1
    else :
        freq[i] = 1 
print(freq)
max_freq = max(freq , key=freq.get)  

print(f"Most frequent no {max_freq}") 



# Most frequent character
list1 = input("Enter character ").split()

freqch = {}

for ch in list1:
    if ch in freqch:
        freqch[ch] += 1
    else :
        freqch[ch] = 1 
print(freqch)
max_freqch = max(freqch , key=freqch.get)  

print(f"Most frequent character {max_freqch}") 
