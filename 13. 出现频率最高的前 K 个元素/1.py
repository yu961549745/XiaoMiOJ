import sys


def solve(a, n):
    m = dict()
    for v in a:
        if v in m:
            m[v] += 1
        else:
            m[v] = 1
    l = list(m.items())
    l = sorted(l, key=lambda x: (-x[1], x[0]))
    return [l[k][0] for k in range(n)]


for line in sys.stdin:
    line = line.strip()
    a, n = line.split(' ')
    a = eval('[%s]' % a)
    n = int(n)
    print(','.join(map(str, solve(a, n))))
