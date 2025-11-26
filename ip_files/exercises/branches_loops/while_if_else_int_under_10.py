#while_if_else_int_under_10.py    17Oct2024  crs
max_a = 99
print("Testing while if - else on integers under", max_a)
a = max_a-1 # So we pass the first test
while a < max_a:
    inp = input("Enter integer a:")
    a = int(inp)
    inp = input("Enter integer b:")
    b = int(inp)
    if a > b:
        print("a:",a,"is > b:",b)
    else:
        print("a:",a,"IS NOT > b:",b)
print("a:",a,"b:",b, "Quitting")
    

