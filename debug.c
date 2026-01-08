#include <stdio.h>

int main() {

// Print

#include <stdio.h>
int x = 42;
printf("DEBUG: x = %d\n", x);

// Check Pointers

int *ptr = malloc(sizeof(int));
if(ptr == NULL) {
    printf("Memory allocation failed!\n");
}

// Assertion

#include <assert.h>
int a = -1;
assert(a >= 0);  // program stops if false

    return 0;
}