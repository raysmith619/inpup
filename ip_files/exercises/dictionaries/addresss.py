 #addresss.py   16Aug2024  crs
""" address as a dictionary
"""
add1 = {"city_town": "Watertown",
         "street" : "Bellview",
         "number" : 1234}
print("add1:", add1)
print("city:", add1["city_town"])
print("street:", add1["street"])
print("number:", add1["number"])

new_city = "Belmont"
print("Change city to ", new_city)
add1["city_town"] = new_city
print("add1:", add1)

name = "street"
print("Access element name:", name)
print("add1[", name, "]  = ", add1[name])

name = "What's up?"
print("Access element name:", name, "via ", "add1[", name, "]", sep= "" )
print("add1[", name, "]  = ", add1[name])
