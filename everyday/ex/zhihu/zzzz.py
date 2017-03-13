def is_prime(n):
    for i in range(2, n / 2 + 1):
        if n % i == 0:
            return
    else:
        return n


results = map(is_prime, range(2, 101))
print [i for i in results if i]

