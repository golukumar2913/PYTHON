# Grade Calculator
Marks = int(input("Enter Yous Marks "))

if Marks > 100:
   print("Please Enter your Marks and verify again")
   exit()

if Marks >= 90 :
    grade = "A"
elif Marks >= 80:
   grade = "B" 
elif Marks >= 70:
   grade = "c"  
elif Marks >= 60:
   grade = "D"  
else:
   grade = "F"           

print(grade) 