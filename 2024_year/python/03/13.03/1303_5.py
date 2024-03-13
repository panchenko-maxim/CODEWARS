"""
Grade book
Complete the function so that it finds the average of 
the three scores passed to it and returns the letter value 
associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
Tested values are all between 0 and 100. Theres is no need 
to check for negative values or values greater than 100.

"""


def get_grade(s1, s2, s3):
    average_rating = (s1 + s2 + s3) / 3
    return 'A' if 90 <= average_rating <= 100 else 'B' if 80 <= average_rating < 90 else 'C' if 70 <= average_rating < 80 else 'D' if 60 <= average_rating < 70 else 'F'