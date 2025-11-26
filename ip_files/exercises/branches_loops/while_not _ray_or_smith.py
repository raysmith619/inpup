#while_not_ray_or_smith    17Oct2024  crs
print("Go until ray or smith entered - the break command")
while True:     # until I say
    inp = input("Enter name:")
    if inp == "ray":
        break   # break out of loop

    if inp == "smith":
        break

    print(inp, "is neither ray nor smith")    

print(inp, "- You got it!")
