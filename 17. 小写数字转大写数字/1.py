import sys

a = '佰拾亿仟佰拾万仟佰拾'
b = '零壹贰叁肆伍陆柒捌玖'


def solve(x):
    if int(x) == 0:
        print('零元整')
        return
    n = len(x)
    s = 11-n
    hasZero = False
    r = ''
    for k in range(n):
        y = int(x[k])
        if y == 0:
            if s+k == 2 or s+k == 6:
                hasZero = False
                print(a[s+k], end='')
            else:
                hasZero = True
        else:
            if hasZero:
                print('零', end='')
            hasZero = False
            print(b[y], end='')
            if k != n-1:
                print(a[s+k], end='')
    print('元整')


for line in sys.stdin:
    solve(line.strip())
