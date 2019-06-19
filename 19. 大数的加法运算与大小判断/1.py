import sys

for line in sys.stdin:
    line = line.strip()
    r = eval(line)
    if isinstance(r, bool):
        if r:
            print('Y')
        else:
            print('N')
    else:
        print(r)
