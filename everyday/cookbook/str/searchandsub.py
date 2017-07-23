import re

text = "Today is 11/27/2012. PyCon starts 3/13/2013."

datepattern = re.compile(r'(\d+)/(\d+)/(\d+)')
a = datepattern.sub(r'\3-\1-\2', text)
print(a)
