# Electricity Bill Calculator

Previous = int(input("Enter Previous unit = "))
Current = int(input("Enter Current Unit = "))
Rate = int(input("Enter Rupee per Unit = "))

# unit = Current - Previous
# bill = unit * Rate 

bill = (Current - Previous) * Rate

print ("Your Bill = ",bill)