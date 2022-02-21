# pass-arguments.py

import sys

print('Number of arguments: ', len(sys.argv),
        'arguments.')
print('Argument List', str(sys.argv))
print('The number of arguments is taken from the second argument.')
print('Remember that in an array [0] is the first one, [1] is the second one.')
number_iterations = sys.argv[1]
f = open('output2.txt', 'w')
for i in range(int(number_iterations)):
    if i < 5:
        f.write("The following number is less than 5")
    else:
        f.write("The following number is great than or equal to 5")
    f.write(str(i))
f.close()
print("look inside your folder...")
