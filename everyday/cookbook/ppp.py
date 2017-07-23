from collections import Counter
from collections import defaultdict

def solution(A):
    c = Counter(A)
    repeat = [i for i in c if c[i] > 1]
    ddict = defaultdict(list)
    for i in range(len(A)):
        ddict[A[i]].append(i)
    dis = [max(ddict[i]) -  min(ddict[i]) for i in ddict if len(ddict[i]) > 1]
    return max(dis)










A = [1, 2, 3, 4, 5, 6, 2, 6, 1, 7, 5, 7, 3]
print(solution(A))
