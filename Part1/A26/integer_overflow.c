#include <stdio.h>
#include <limits.h>

int main(void) {
    unsigned int x = UINT_MAX;

    printf("Maximum unsigned int value: %u\n", x);

    x = x + 1;

    printf("Value after adding 1: %u\n", x);
    printf("This demonstrates integer overflow, where the value wraps around.\n");

    return 0;
}