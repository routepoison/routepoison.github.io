# read_file.py 

#
# An example of reading a file in your 
# current working directory ot print and
# manipulate the output.
#

# Define the path and file into a variable, 'filepath'.

filepath = "./pico.txt"
i = 1

#
# 'with' keyword is used to close the file automatically
# after reading, also, to handle possibl exceptions when
# executing.
#

with open(filepath, "r") as my_file:
    for line in my_file:
        print(i)
        print(line)
        i += 1
