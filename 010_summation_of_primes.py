#010 - Summation of Primes

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all primes below 2 million.

# use algorithm from problem 007
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

limit = 2 * (10**6)
primes = SieveOfAtkin(limit)
print(f"Sum of primes: {sum(primes)}")
#142913828922