# Sample lists
list1 = [1, 2, 3, 4, 5, 2, 8, 10]
list2 = [5, 6, 7, 8, 9, 5, 10]
list3 = [8, 9, 10, 11, 12, 8, 10]

# Find duplicates using sets
common_elements = set(list1) & set(list2) & set(list3)

# Convert the result to a list for printing
common_elements_list = list(common_elements)

# Check if there are duplicates
if common_elements_list:
    print("Common elements (duplicates) in the three lists:", common_elements_list)
else:
    print("No common elements found.")
