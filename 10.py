# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

n = 2000000
s = range(3, n, 2)
i = 0
m = 3
h = len(s)
while m <= n**0.5:
    if s[i]:
        j = (m*m-3)//2
        s[j] = 0
        while j < h:
            s[j] = 0
            j += m
    i += 1
    m = 2*i+3
print sum(s)+2
