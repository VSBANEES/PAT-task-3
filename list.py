original_list = [10, 501, 22, 37, 100, 999, 87, 351]

even_numbers = [] #Initialize empty list for even numbers
odd_numbers = [] #initialize empty list for odd numbers

# Iterate through the original list
for number in original_list:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# Print the results
print("Original List:", original_list)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
