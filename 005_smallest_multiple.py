#005 - Smallest Multiple -UNSOLVED

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder.What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?

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

#generates all prime factors for a number
def generate_prime_factors(num):
    prime_factors = []
    if is_prime(num):
        prime_factors.append(num)
        return prime_factors
    if num%2==0:
        prime_factors.append(2)
        other_factor = int(num / 2)
        prime_factors = prime_factors + generate_prime_factors(other_factor)
    if num%3==0:
        prime_factors.append(3)
        other_factor = int(num / 3)
        prime_factors = prime_factors + generate_prime_factors(other_factor)
    #if num%5==0:
    #    prime_factors.append(5)
    for i in range(3, int(num**0.5)+1, 2):
        #check if i is a factor of num
        if num % i == 0:
            if is_prime(i):
                prime_factors.append(i)
                other_factor = int(num / i)
                prime_factors = prime_factors + generate_prime_factors(other_factor)
            else:
                prime_factors = prime_factors + generate_prime_factors(i)
    return prime_factors


lower = 1
upper = 20

prime_factors = []
for i in range(lower, upper+1):
    prime_factors = prime_factors + generate_prime_factors(i)

#convert to set then back to list to get distinct values
prime_factors = list(set(prime_factors))
product = 1
for x in prime_factors:
    product = product * x

print(f"Smallest multiple: {product}")
#9699690 - incorrect :(
# ^its not divisible by all of 1-20