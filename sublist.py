given_list = [4, 2, -3, 1, 6]

# Iterate through the list to find sublists
for i in range(len(given_list)):
    current_sum = 0
    for j in range(i, len(given_list)):
        current_sum += given_list[j]

        # Check if the current sublist has a sum of zero
        if current_sum == 0:
            result_sublist = given_list[i:j + 1]
            print(f"Sublist with sum zero found: {result_sublist}")
        
