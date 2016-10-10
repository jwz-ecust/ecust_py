def tribonacci(l,n):
    if n == 0:
        return []
    else:
        while True:
            if len(l) > n:
                return l[:n]
            else:
                l.append(sum(l[-3:]))

print tribonacci([1,2,3],10)