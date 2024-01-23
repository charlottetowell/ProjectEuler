#007 - 10001st Prime

# By listing the first six prime numbers, 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?


### initial research:
# Sieve of Eratosthenes (good for finding smaller prime numbers) - O(Nlog(log(N)))
# > marks off multiples of primes
# Sieve of Atkin - O(N) complexity for N primes <----
# > marks off multiples of squares of primes
# Sive of Sundaram - O(Nlog(N))
# > variant of Earosthenes


# https://www.geeksforgeeks.org/sieve-of-atkin/
def SieveOfAtkin(limit):
    primes = []
    # 2 and 3 are known
    # to be prime
    if limit > 2:
        primes.append(2)
    if limit > 3:
        primes.append(3)

    # Initialise the sieve
    # array with False values
    sieve = [False] * (limit + 1)
    for i in range(0, limit + 1):
        sieve[i] = False

    '''Mark sieve[n] is True if
	one of the following is True:
	a) n = (4*x*x)+(y*y) has odd
	number of solutions, i.e.,
	there exist odd number of
	distinct pairs (x, y) that
	satisfy the equation and
	n % 12 = 1 or n % 12 = 5.
	b) n = (3*x*x)+(y*y) has
	odd number of solutions
	and n % 12 = 7
	c) n = (3*x*x)-(y*y) has
	odd number of solutions,
	x > y and n % 12 = 11 '''
    x = 1
    while x * x <= limit:
        y = 1
        while y * y <= limit:

        	# Main part of
            # Sieve of Atkin
            n = (4 * x * x) + (y * y)
            if (n <= limit and (n % 12 == 1 or n % 12 == 5)):
                sieve[n] ^= True

            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                sieve[n] ^= True

            n = (3 * x * x) - (y * y)
            if (x > y and n <= limit and n % 12 == 11):
                sieve[n] ^= True
            y += 1
        x += 1

	# Mark all multiples of
	# squares as non-prime
    r = 5
    while r * r <= limit:
        if sieve[r]:
            for i in range(r * r, limit+1, r * r):
                sieve[i] = False
        r += 1

    #get primes from sieve
    for a in range(5, limit+1):
        if sieve[a]:
            #print(a, end=" ")
            primes.append(a)

    return primes


#test high limits to find 10,001st prime
n = 10001
limit = 150000
primes = SieveOfAtkin(limit)
#print(len(primes))

print(primes[n-1]) #104743 is the 10,001st prime