# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 09:04:41 2024

@author: Student
"""
from sympy import symbols, Eq, solve

# Define the variables
x = symbols('x')

# Coefficients of the quadratic equation
a = 1
b = -3
c = 2

# Create the quadratic equation
equation = Eq(a*x**2 + b*x + c, 0)

# Solve the quadratic equation
solutions = solve(equation, x)

# Display the solutions
if len(solutions) == 2:
    print("Root 1:", solutions[0])
    print("Root 2:", solutions[1])
elif len(solutions) == 1:
    print("Root:", solutions[0])
else:
    print("No real roots")
