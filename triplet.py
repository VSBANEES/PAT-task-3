given_list = [10, 20, 30, 9]
target_sum = 59

# Sort the list
given_list.sort()

# Iterate through the list to find triplets
for i in range(len(given_list) - 2):
    left, right = i + 1, len(given_list) - 1

    while left < right:
        current_sum = given_list[i] + given_list[left] + given_list[right]

        if current_sum == target_sum:
            # Triplet found
            result_triplet = [given_list[i], given_list[left], given_list[right]]
            print(f"Triplet with sum {target_sum} found: {result_triplet}")
            break
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1
else:
    # No triplet found
    print(f"No triplet found with sum {target_sum}")
