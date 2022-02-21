# try-except.py

#
# Using 'try' and 'except' as try catch
#

num1 = 8
num2 = input("Input the number that will divide: ")
num3 = int(num2)

#
# try-except, diving by 0 will trigger the 'except'
# 

try:
    result = num1 / num3
    print(result)
except ZeroDivisionError:
    print("Do not divide by zero.")
except TypeError:
    print("Your input value must be an integer.")
print("The program executing to do other stuff...")
