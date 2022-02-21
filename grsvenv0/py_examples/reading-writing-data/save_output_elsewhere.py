# save_output_elsewhere.py

#
# if you want to save your output in another file
# you can easily do it in the following manner
#

filepath_read = "pico.txt"
filepath_write = "outputpico.txt"
i = 1

with open(filepath_read, "r") as file_read:
        with open(filepath_write, "w") as file_write:
            for line in file_read:
                file_write.write(str(i) + "\n")
                file_write.write(line + "\n")
                i += 1
print("look inside your folder...")
