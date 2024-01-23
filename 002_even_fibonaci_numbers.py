#002 - Even Fibonacci Numbers

#Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

upper_limit = 4*(10**6) #4 million

def next_fib_num(second_last, last):
    #returns next number in Fibonacci sequence
    return second_last + last


def is_even(num):
    #returns TRUE if num is even
    return num % 2 == 0

#define starting 2 terms
(a, b) = (1, 2)
#define initial sum of even numbers
even_sum = 2

#generate fibonacci numbers until upper limit
while b <= upper_limit:
    c = next_fib_num(a, b)
    #add even numbers to sum
    if is_even(c):
        even_sum += c
    (a, b) = (b, c)

print(f"Sum: {even_sum}")