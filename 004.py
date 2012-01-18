# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

results = []
for a in range(999,100,-1):
    for b in range(999,100,-1):
        if str(a*b) == str(a*b)[::-1]:
            results.append(a*b)
results.sort()
print results[-1]
