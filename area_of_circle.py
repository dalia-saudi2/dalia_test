# CircleArea.py

import math

def area_of_circle(radius):
    
    if radius <0 :
        raise ValueError("radius can't be negative")
    return math.pi*(radius**2)
    
