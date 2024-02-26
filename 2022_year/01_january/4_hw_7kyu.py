"""
Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built
with the sides of given length and false in any other case.
(In this case, all triangles must have surface greater than 0 to be accepted).
"""
def is_triangle(a, b, c):
    return all([a + b > c, a + c > b, b + c > a])
print(is_triangle(1,2,2))

# FOR EXAMPLE
# def is_triangle(a, b, c):
#     a, b, c = sorted([a, b, c])
#     return a + b > c

# EXAMPLE 2
# return a < b + c and b < a + c and c < a + b
