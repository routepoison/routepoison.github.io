# Python Samples and Tutorials

##  Lists

# 
# Create a list in variable 'my_list'
#

my_list = ["I", "Love", "picoCTF"]
print(my_list)
print("\n")

#
# Print the length, or number of items in 'my_list'
#

print("The length of list 'my_list' is: ", len(my_list))

#
# Create an unordered list
#

unordered_list = ["this", "is", "not", "ordered", "alphabetically"]
# Put the 'unordered_list' in a variable, 'my_ordered_list' and use
# the '.sort()' function to sort it alphabetically
my_ordered_list = unordered_list.sort()
# Proceed to iterate through the list using a 'for' loop.
for i in unordered_list:
    print(i)

#
# Create a list of numbers and print them in reverse.
#

num_list = [3,1,5,2,6,4,7,9,10,0]
print("\nPrint variable 'num_list' (unordered list of numbers: ", num_list)
# now reverse the list:
reversed_list = list(reversed(num_list))
print("\nPrint variable 'num_list' (reversed): ", reversed_list)

#
# EOF
#
