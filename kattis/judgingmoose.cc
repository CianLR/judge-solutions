#include <stdio.h>

int main() {
  int L, R;
  scanf("%d %d", &L, &R);
  if (L == 0 && R == 0) {
    printf("Not a moose\n");
  } else if (L == R) {
    printf("Even %d\n", L + R);
  } else {
    printf("Odd %d\n", 2 * (L > R? L : R));
  }
}

