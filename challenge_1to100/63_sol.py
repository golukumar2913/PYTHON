# Check anagram

one = input("Enter first string ")
two  = input("Enter 2nd string ")

if sorted(one) == sorted(two):
    print("Anagram")
else:
    print("Not anagram") 
