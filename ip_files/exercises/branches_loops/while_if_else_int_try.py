#while_if_else_int_try.py    31Oct2024  crs
#                           17Oct2024  crs
print("Testing while if - else on integers with try")
while True:
    while True:         # Continue until OK input
        try:
            a = int(input("Enter integer a:"))
            break
        
        except:
            print("I don't understand")
            continue
    
    while True:
        try:
            b = int(input("Enter integer b:"))
            break
        except:
            print("I don't understand")
            continue
    
    if a > b:
        print("a:",a,"is > b:",b)
    else:
        print("a:",a,"IS NOT > b:",b)
    

