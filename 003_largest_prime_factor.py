#003 - Largest Prime Factor

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

def is_prime(n):
    #returns TRUE if n is prime
    if n==2 or n==3:
        return True
    if n%2==0 or n<2:
        return False
    #loop through odd numbers only
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0:
            return False    

    return True

num = 600851475143
sqrt = num**0.5
prime_factors = []

#loop through odd numbers up until the square root
for i in range(3, int(sqrt)+1, 2):
    #check if i is a factor of num
    if num % i == 0:
        if is_prime(i):
            prime_factors.append(i)

print(f"Max: {max(prime_factors)}")
