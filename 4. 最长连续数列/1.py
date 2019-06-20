import sys


def solve(a):
    m = dict()  # m[k] 记录 以 k 开头的连续数列的长度
    for v in a:
        if not (v in m):
            m[v] = 1
            if v+1 in m:
                m[v] += m[v+1]
            x = v
            while x-1 in m:
                m[x-1] += m[v]
                x -= 1
    # print(m)
    return max(m.values())


for line in sys.stdin:
    a = eval('[%s]' % line.strip())
    print(solve(a))
