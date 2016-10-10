def validate_pin(pin):
    list = [str(i) for i in range(10)]
    return len(pin) == 4 and all([ (i in list) for i in pin])


print validate_pin('1234')
print validate_pin('1a11')
