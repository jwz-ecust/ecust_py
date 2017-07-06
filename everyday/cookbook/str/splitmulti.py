import re
line = "asdf fjdk; afed, fjek,asdf, foo"

a = re.split(r'[;,\s]\s*', line)
print(a)



choices = ('http:', 'ftp:', "https:")
url = "https://www.google.com"
print(url.startswith(choices))
