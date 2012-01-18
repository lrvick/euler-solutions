# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.

# What is the 10001st prime number?

c = 2
p = 0
while p < 10001:
    for y in range(2,(c/2)+1):
        if c%y==0:
            break
    else:
        p +=1
    c+=1
print c-1
