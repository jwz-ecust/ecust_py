def to_weird_case(string):
    list = string.split(' ')
    f = lambda i,j: i.upper() if j%2 == 0 else i.lower()
    res = []
    for word in list:
        res.append(''.join([f(word[i],i) for i in range(len(word))]))
    return (' ').join(res)


print to_weird_case('TeST zzz zzz jw z wa')