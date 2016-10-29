def divisors(integer):
    if integer in (0,1):
        return None
    else:
        res = []
        for i in range(2,integer):
            if integer%i == 0:
                res.append(i)
        if len(res)==0:
            print  "{} is prime".format(str(integer))
        else:
            return res



print divisors(10)
print divisors(11)
print divisors(13)
print divisors(14)