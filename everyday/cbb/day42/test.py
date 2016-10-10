def next_bigger(n):
    i = 0
    s = [i for i in str(n)][::-1]
    for i in range(len(s)):
        if i == len(s)-1:
            index = -1
            break
        elif s[i]>s[i+1]:
            index = i
            break
        else:
            i = i+1
    if index == -1:
        print "the number is the biggest"
        return -1
    else:
        ff = s[:index]+[s[index+1]]+[s[index]]+s[index+2:]
        return int(''.join(ff[::-1]))

print next_bigger(1232312412)