class Chess(float):
    def __str__(self):
        return "Muenster"
    def __repr__(self):
        return "Stilton"
chunk = Chess(-123.4)

print str(chunk)
print repr(chunk)
print int(chunk)
print "%s\t%r\t%d" %(chunk,chunk,chunk)
