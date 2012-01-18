# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

i = 1
c = 20
for x in range(c,1,-1):
    for y in range(2,(x/2)+1):
        if x%y==0:
            break
    else:
        i *= x
s = i
while True:
    for x in range(c,1,-1):
        if s%x != 0:
            break
    else:
        print s
        break
    s += i
