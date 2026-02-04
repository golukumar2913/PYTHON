score = 100

if score > 100:
   print("Please Enter your Marks and verify again")
   exit()

if score >= 90 :
    grade = "A"
elif score >= 80:
   grade = "B" 
elif score >= 70:
   grade = "c"  
elif score >= 60:
   grade = "D"  
else:
   grade = "F"           

print(grade)   