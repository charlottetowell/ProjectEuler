#001 - Multiples of 3 and 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6, and 9. The sum of these multiples is 23. Find the sum of 
# all the multiples of 3 or 5 below 1000.


def is_multiple(num, mul):
    #returns TRUE if num is a multiple of mul
    return num % mul == 0

found_multiples = []
upper_limit = 1000

#check all natural numbers up to upper_limit
for i in range(upper_limit):
    #check if multiple of 3 or 5
    if is_multiple(i, 3) or is_multiple(i, 5):
        found_multiples.append(i)

#sum all found multiples
print(f"Sum: {sum(found_multiples)}")