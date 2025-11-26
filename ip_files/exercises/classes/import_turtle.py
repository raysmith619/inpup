#import_turtle.py     30Dec2021  crs, Author
"""
import <module>
Access each turtle function via turtle.<member_name>
"""
import turtle			# Bring in module
side = 100
angle = 60
for i in range(6):
    turtle.forward(side)	# Use module
    turtle.right(angle)
    
