original_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Create two lists for even and odd numbers
even_numbers = [num for num in original_list if num % 2 == 0]
odd_numbers = [num for num in original_list if num % 2 != 0]

# Print the results
print("Original List:", original_list)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
