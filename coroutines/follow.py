import time

def follow(f):
    f.seek(0,2)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

f = open('file.txt')
for line in follow(f):
    print line,
