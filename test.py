a=[]

for n in range(2, 100000000):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        # loop fell through without finding a factor
        a.append(n)
print a