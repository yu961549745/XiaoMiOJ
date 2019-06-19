import sys
import math

a = '1234567898765432'
for line in sys.stdin:
    k = int(line.strip())
    n = math.ceil((math.sqrt(1+8*k)-1)/2)
    print(a[(k - (n-1)*n // 2 - 1) % 16])
