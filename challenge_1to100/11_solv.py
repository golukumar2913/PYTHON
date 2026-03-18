# Check vowel or consonant and use exit function
char = input("Enter Character ")
char_lower = char.lower()

vowels = ['a', 'e', 'i', 'o', 'u']

if len(char) != 1:
    print( "Invalid input: Please enter a single character.")
    
elif not char.isalpha():
    print (f"'{char}' is not an alphabet character.")   
    
else:
     if char_lower in vowels:
        print(f"'{char}' is a vowel.")  
     else:
        print( f"'{char}' is a consonant." )   


exit()        

print("golu")        