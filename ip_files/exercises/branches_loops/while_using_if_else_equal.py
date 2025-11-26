#while_using_if_else_equal.py    14Nov2024  crs
print("Testing if - else, ==,<,> in a while loop")

while True:
    a_str = input("Enter a_str:")
    b_str = input("Enter b_str:")
    if a_str == b_str:
        print("a_str:", a_str, "is ==", "b_str:", b_str)
    else:
        print("a_str:", a_str, "is !=", "b_str:", b_str)
        if a_str < b_str:
            print("a_str:", a_str, "is <", "b_str:", b_str)
        if a_str > b_str:
            print("a_str:", a_str, "is >",  "b_str:", b_str)
    

