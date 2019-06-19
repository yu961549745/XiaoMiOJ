import sys
import math


def LTN(N):
    if N == 0:
        return 0
    L = math.floor(math.log10(N))
    return round(
        L*N**2/2 + 3*L*N/2+N**2/2-10*N*10**L/9 + L +
        29*N/18 + 50*100**L/99 - 5*10**L/3 + 115/99
    )


def LSn(n):
    if n == 0:
        return 0
    M = math.floor(math.log10(n))
    return round(n*M+M-10**(M+1)/9 + n+10/9)


def bs(f, k, a, b):
    while b-a > 1:
        c = (a+b)//2
        if f(c)-k < 0:
            a = c
        else:
            b = c
    return a


def solve(K):
    N = bs(LTN, K, 0, 10**8)  # LTN(N)<K<=LTN(N+1)
    R = K-LTN(N)  # K 在 S[N+1] 的第 R 位 (R>=1)
    n = bs(LSn, R, 0, LSn(N+1))  # LSn(n)<R<=LSn(n+1)
    s = R-LSn(n)  # K 在数字 n+1 的第 s 位 (s>=1)
    return str(n+1)[s-1]


for line in sys.stdin:
    K = int(line.strip())
    print(solve(K))
