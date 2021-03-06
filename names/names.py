# from binary_search_tree import BinarySearchTree
import time
import sys

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# #first pass optimization 

# for name_1 in names_1:
#         if name_1 in names_2:
#             duplicates.append(name_1) 

# STRETCH: second pass optimization with Binary Search

# Run time using dict() and binary search tree travasal method has reduced the runtimee drastically but using in built dic() method is faster than implementing binary search

check = dict()
for name1 in names_1:
    check[name1] = True
for name2 in names_2:
    if name2 in check:
        duplicates.append(name2)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
