def make_readable(seconds):
    if seconds > 359999:
        return 'error'
    else:
        hour = int(seconds/3600)
        minite = int((seconds-hour*3600)/60)
        second = int(seconds-hour*3600-minite*60)
        return "%02d:%02d:%02d" %(hour,minite,second) # return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

print make_readable(0)
print make_readable(5)
print make_readable(60)
print make_readable(86399)
print make_readable(359999)