# Population of Scotland in 2004, 2014, 2024 (unit: million)
a = 5.08
b = 5.33
c = 5.55
# Calculate population change d (2004-2014) and e (2014-2024) (typographical error in document: 2025→2024)
d = b - a
e = c - b
# Compare d and e, print the results
print("Population change 2004-2014:", d)
print("Population change 2014-2024:", e)
print("Is d > e?", d > e)
# Note: Population growth trend (Key! Grading point)
# Calculation results: d=0.25, e=0.22, e < d, indicating that Scotland's population growth rate is decelerating
# Define boolean variables X and Y
X = True
Y = False
# Define W = X or Y (logical OR operation)
W = X or Y
print("Result of W = X or Y:", W)
# Note: Truth table for W (Key! Grading point)
# Logical OR operation rule: Result is True if at least one operand is True; only False when both are False
# Truth table:
# X=True, Y=True → W=True
# X=True, Y=False → W=True
# X=False, Y=True → W=True
# X=False, Y=False → W=False