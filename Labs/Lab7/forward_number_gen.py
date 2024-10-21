# This program generates a list of numbers and writes them to a file.
import random

##### Generate list of numbers #####
n = [100, 500, 1000, 2000]
for i in n:
    L = [i for i in range(i)]

    ##### Create file to write to #####
    f = open(f"./numbers.txt", "w")

    ##### Write numbers to file #####
    for item in L:
        f.write(str(item))
        f.write(" ")

    #### Close the file ####
    f.close()

    #### Wait for user to press enter ####
    input(f"Generated {i} numbers. Press enter to continue...")

