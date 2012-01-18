# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

factors = []

n = 600851475143

c = 2

while c <= int(n**0.5):
    if n % c == 0:
        prime = True
        for x in range(3,int(c**0.5)+1,2):
            if c % x == 0:
                prime = False
                break
        if prime:
            factors.append(c)
    c += 1

print factors[-1]
