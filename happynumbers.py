def is_happy_number(n): #This function is used to check whether the given number is a happy number
    seen_numbers = set() #empty set for happy numbers

    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = sum(int(digit)**2 for digit in str(n))

    return n == 1

def count_happy_numbers(numbers):
    count = 0
    for number in numbers:
        if is_happy_number(number):
            count += 1
    return count

# Given list
numbers_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Count the number of happy numbers in the list
happy_numbers_count = count_happy_numbers(numbers_list)

print("Original List:", numbers_list)
print("Number of Happy Numbers:", happy_numbers_count)
