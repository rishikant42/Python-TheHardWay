import time

def unix_head(f):
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


f = open('file.txt')

gen = unix_head(f)

for i in gen:
    print i
