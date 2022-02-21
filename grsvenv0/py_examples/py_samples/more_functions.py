# More Playing with Functions

# Just a reminder you can issue a newline in your code(adds a tab):
# print("Input the number of \
#        iterations:")

("Input the number of iterations:")
num_iterations = input("Input the number of iterations: ")
#
# Notice the typecast into 'int' again.
#
for i in range(int(num_iterations)):
        if i < 5:
            print("The following number is less than 5")
        else:
            print("The following number is greater than or equal to 5")
print(i)
