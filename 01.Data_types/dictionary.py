# key based 
# it based on key value pair
# it write on curly braces {}

username = {
    "name":"Golu",
    "age":23,
    "course":"Python",
    "is_Active" : True
}

# print(username)

# Dictionary access

print(username["name"])
print(username.get("name"))

username["gender"] = "male" 
print(username)

tea_shop = {
    "chai": {"masala": "testy", "lemon": "kadwa"},
    "tea": {"green": "mild", "black": "strong"}
}

print(tea_shop["chai"])
print(tea_shop["chai"]["masala"])

# loop on dictionary data type 

for key , value in username.items():
    print(key , value)


squared_num = {x : x**2 for x in range(6)}
print(squared_num)