 #addresss_checking.py   16Aug2024  crs
""" address as a dictionary
+ Check if key is present
"""
add1 = {"city_town": "Watertown",
         "street" : "Bellview",
         "number" : 1234}
print("add1:", add1)
print("city:", add1["city_town"])
print("street:", add1["street"])
print("number:", add1["number"])

new_city = "Belmont"
print("\nChange city to ", new_city)
add1["city_town"] = new_city
print("add1:", add1)

name = "street"
print("\nAccess element name:", name)
print("add1[", name, "]  = ", add1[name])

name = "What's up?"
print("\nAccess element name:", name, " via ", "add1[", name, "]", sep= "" )
print("Check if ", name, "is a valid key")
if name in add1:
    print("add1[", name, "]  = ", add1[name])
else:
    print(name, " is not a key in add1 (", add1, ")", sep="")
    
