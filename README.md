# homework1
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 08:20:08 2024

@author: Student
"""

import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root, None
    else:
        return None, None

# Example usage
a = 1
b = 5
c = 6

root1, root2 = solve_quadratic(a, b, c)

if root1 is not None and root2 is not None:
    print("Roots:", root1, root2)
else:
    print("No real roots")
