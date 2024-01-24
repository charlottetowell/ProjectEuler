#009 - Special Pythagorean Triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c,
# for which a^2 + b^2 = c^2.
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

sumabc = 1000

#c = sqrt(a^2 + b^2)
#a + b + c = 1000
#b = 1000 - a - c
#c = sqrt(a^2 + (1000-a-c)^2)

### FIRST ATTEMPT

def generate_pythagorean_triplet(a):
    #given a, returns b,c to form a pythagorean triplet
    #does not return ALL triplets

    #case: a is even
    if a%2 == 0:
        b = a**2 / 2 - 0.5
        c = a**2 / 2 + 0.5
        return b, c
    #case: a is odd
    else:
        b = a**2 / 2 - 1
        c = a**2 / 2 + 1
        return b,c

found = False
i = 0
starting_num = 100
while not found:
    if i >= 1000: #stop failsale
        print("stopped")
        found = True
        break
    else:
        a = starting_num + i
        b, c = generate_pythagorean_triplet(a)
        if a + b + c == sumabc:
            print(a)
            found = True
            break
        else:
            i += 1

### SECOND ATTEMPT

# generate all triplets with c below a limit
def pythagoreanTriplets(limits) : 
    c, m = 0, 2
    while c < limits : 
        for n in range(1, m) : 
            a = m**2 - n**2
            b = 2 * m * n 
            c = m**2 + n**2

            if c > limits : 
                break

            #check if triplet terms sum to 1000
            if a + b + c == sumabc:
                return a,b,c

        m += 1


limit = 1000
a,b,c = pythagoreanTriplets(limit) 
print(f"Product: {a*b*c}")