def grep(pattern):
    print "Searching for",pattern
    while True:
        line = (yield)
        if pattern in line:
            print line
