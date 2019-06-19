import sys

for line in sys.stdin:
    line = line.strip()
    try:
        print(eval(line.replace('/', '//')))
    except Exception:
        print('err')
