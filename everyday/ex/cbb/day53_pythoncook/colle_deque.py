from collections import deque

def search(lines,pattern,history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li,previous_lines
        previous_lines.append(li)
        print previous_lines
lines = ['z','k','j','w']

pattern = 'z'
for i in search(lines,pattern):
    print i