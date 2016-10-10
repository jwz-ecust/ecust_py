import sys
import time
from collections import deque

loading = deque('>--------------------')

while True:
    print '\r%s' % ''.join(loading)
    loading.rotate()
    sys.stdout.flush()
    time.sleep(0.8)