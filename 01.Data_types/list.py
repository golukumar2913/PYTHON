# based on Index
# written in brackets []
# mutable

tea_list = ["Lemon", "Herbel", "Ginger", "Masala"]

# access tea_list
print(tea_list[0])
print(tea_list[-1])

# add tea in tea_list last index
tea_list.append("Black")
tea_list.insert(3, "white")
print(tea_list)

# part nikalana
print(tea_list[1:3])
print(tea_list[0:4:3])

# loop on tea_list
for tea in tea_list:
    print(tea)

# -----------------------------
# EXTRA LIST FUNCTIONS PRACTICE

# remove an item by value
tea_list.remove("Herbel")  # removes 'Herbel'
print("\nAfter remove():", tea_list)

# pop an item by index (default last)
popped_tea = tea_list.pop()  
print("Popped tea:", popped_tea)
print("After pop():", tea_list)

# count occurrences
tea_list.append("Ginger")
print("Count of 'Ginger':", tea_list.count("Ginger"))

# find index
print("Index of 'white':", tea_list.index("white"))

# sort the list
tea_list.sort()
print("Sorted list:", tea_list)

# reverse the list
tea_list.reverse()
print("Reversed list:", tea_list)

# clear the list
tea_list.clear()
print("Cleared list:", tea_list)
