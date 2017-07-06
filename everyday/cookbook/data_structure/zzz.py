from collections import ChainMap

values = ChainMap()
values['x'] = 1
print(values)
values = values.new_child()
values['x'] = 2
print(values)
