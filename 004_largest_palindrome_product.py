#004  - Largest Palindrome Product

# A palindromic number reads the same both ways. The largest palindrome made from the product of
# two 2-digit numbers is 9009 = 91 * 99
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(num):
    #returns TRUE if num is palindromic
    return str(num) == str(num)[::-1]

num_digits = 3
upper_limit = int("9"*num_digits)
lower_limit = int("1" + "0"*(num_digits-1))

palindromes = []
multipliers = []

#generate all palindrome products from 3 digit numbers
for a in reversed(range(lower_limit, upper_limit)):
    for b in reversed(range(lower_limit, upper_limit)):
        product = a*b
        if is_palindrome(product):
            palindromes.append(product)
            multipliers.append((a,b))

#print max palindrome and corresponding multipliers
index = palindromes.index(max(palindromes))
print(f"Largest palindrome: {max(palindromes)} from {multipliers[index][0]} * {multipliers[index][1]}")