#include <stdio.h>

int main() {
    int a,b;
    a=0;
    while (EOF != scanf("%d", &b)) {
        a^=b;
    }
    printf("%d\n",a);
    return 0;
}