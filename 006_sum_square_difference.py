#006 - Sum Square Difference

# The sum of squares of the first ten natural numbers is,
#           1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#           (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of squares of the first
# ten natural numbers and the square of the sum is,
#           3025 - 385 = 2640
# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.


def sum_of_squares(upper_limit):
    #returns the sum of squares for the first upper_limit natural numbers
    nums = list(range(1,upper_limit+1))
    square_nums = [ x**2 for x in nums]
    return sum(square_nums)

def square_of_sum(upper_limit):
    #returns the square of the sum for the first upper_limit natural numbers
    nums = list(range(1,upper_limit+1))
    sumn = sum(nums)
    return sumn**2

def sum_square_difference(upper_limit):
    return square_of_sum(upper_limit) - sum_of_squares(upper_limit)

upper_limit = 100
print(f"Sum of squares: {sum_of_squares(upper_limit)}")
print(f"Square of sum: {square_of_sum(upper_limit)}")
print(f"The sum square difference: {sum_square_difference(upper_limit)}")