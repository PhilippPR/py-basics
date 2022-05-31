"""
An Integer is a class that represents an integer value.
Integer are whole numbers. Like: 1 / 900 / -3 / -400

Reminder: 
    - An Integer is a whole number.
    - An Integer is not a float.
    - in Python u user "." for decimal numbers. (not ",")
"""

print(int(12))
print(int(12.5)) # This will round the value to the nearest integer
print(int(-12))
print(int(-12.4)) # This will round the value to the nearest integer
print(int(5))
print(int(5.12)) # This will round the value to the nearest integer
print(int(-5)) 
print(int(-5.6)) # This will round the value to the nearest integer


# if u use a comma in the int() function, u will get an error. (TypeError: int() can't convert non-string with explicit base)

# if u wanne have a integer with a , in it u cant use int() for that. You have to use the float() function.