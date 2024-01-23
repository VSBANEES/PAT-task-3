def is_prime(number): #checking the number is prime
    if number < 2: #2 is smallest prime number, so we have started from 2
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

original_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Initialize empty list for prime numbers
prime_numbers = []

# Count and filter prime numbers
for number in original_list:
    if is_prime(number):
        prime_numbers.append(number)

# Print the results
print("Original List:", original_list)
print("Prime Numbers:", prime_numbers)
