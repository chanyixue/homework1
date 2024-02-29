# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 08:20:08 2024

@author: Student
"""

import itertools

# Define the propositions P and Q
propositions = ['F', 'T']

# Generate all combinations of truth values for P and Q
truth_combinations = list(itertools.product(propositions, repeat=2))

# Evaluate the logical operators for each combination
results = []
for p, q in truth_combinations:
    pandq = p == 'T' and q == 'T'
    porq = p == 'T' or q == 'T'
    pandq2 = p and q
    porq2 = p or q
    implies = not p or q
    reverse_implies = not q or p
    equivalence = (not p or q) and (not q or p)
    results.append([p, q, pandq, porq, pandq2, porq2, implies, reverse_implies, equivalence])

# Display the truth table
print("P\tQ\tP ∧ Q\tP ∨ Q\tP ∧ Q\tP ∨ Q\tP → Q\tP ← Q\tP ↔ Q")
for row in results:
    print("\t".join(row))


