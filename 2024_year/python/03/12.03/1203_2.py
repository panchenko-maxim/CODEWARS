"""
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""


def reverse_words(text):
  return ' '.join([''.join(list(el)[::-1]) for el in text.split(' ')])



print(reverse_words("double  spaces"))