a=[]
for n in range(2, 10000):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        # loop fell through without finding a factor
        a.append(n)

print a


b=[1,2,3,4,5,6,7,8,9,10]
b.append(11)
b.insert(3,"x")
print b