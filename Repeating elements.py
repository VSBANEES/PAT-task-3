def find_first_non_repeating_element(nums):
    # Create a dictionary to store the count of each element
    element_count = {}

    # Create a list to maintain the order of elements as they appear
    order_of_appearance = []

    # Iterate through the list to count occurrences and maintain order
    for num in nums:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1
            order_of_appearance.append(num)

    # Find the first non-repeating element
    for num in order_of_appearance:
        if element_count[num] == 1:
            return num

    # If no non-repeating element is found, return None
    return None

input_list = [3, 5, 2, 7, 5, 3, 10, 2, 7, 1]
result = find_first_non_repeating_element(input_list)

if result is not None:
    print(f"The first non-repeating element is: {result}")
else:
    print("No non-repeating element found.")
