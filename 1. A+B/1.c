#include <stdio.h>

int main() {
    long long a, b;
    while (EOF != scanf("%lld%lld", &a, &b)) {
        printf("%lld\n", a + b);
    }
    return 0;
}
