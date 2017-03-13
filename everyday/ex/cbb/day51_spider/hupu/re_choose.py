import re
with open('hupu_photo.html','r') as f:
    while True:
        find_it = re.findall('<a class="ku".*>',f.readline())
