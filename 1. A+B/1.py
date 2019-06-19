import sys

for line in sys.stdin:
    line = line.strip()
    print(eval(line.replace(' ', '+')))
