# Functions.py

## Introductory Review and Refresher of Functions

#
# Define the function with 'def' keyword.
#

def even_odd(x):
        if (x % 2 == 0):
            return True
        else:
            return False

#
# --- 
#

my_num = input("Input a number: ")
#
# Gotcha: despite the tutorial, it did not specify that string
# "my_num, must be cast as an integer from the user input.
#
if even_odd(int(my_num)):
    print("The number is even.")
else:
    print("The number is odd.")
#
# --- [EOF] ---
#


