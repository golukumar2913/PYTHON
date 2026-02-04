
fruits = ["apple", "banana", "orange", "apple"]

unique_items = set()

for item in fruits:
    if item in unique_items:
        print("Duplicate: ", item)
        break
    unique_items.add(item)
print(unique_items)    