from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li.strip()
        previous_lines.append(li)


with open("./zjw") as fu:
    c = fu.readlines()
    for i in search(c, "asd", history=5):
        print(i)
