import re


def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))

    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)


text = """zhang jia wei, chen er bei , chen er bei, zhang yi chen, chen bei bei"""
adict = {'ei': "$$$", 'z': "%", 'b': "B"}

print multiple_replace(text, adict)


print '|'.join(map(re.escape, adict))
