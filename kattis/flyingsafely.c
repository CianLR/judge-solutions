#include <stdio.h>

unsigned int read_uint() {
  unsigned int i = 0;
  char c = getchar_unlocked();
  while (c < 58 && c > 47) {
    i = (i * 10) + (c - 48);
    c = getchar_unlocked();
  }
  return i;
}

// 0.00 second solution
int main() {
  unsigned int a, b, T = read_uint();
  while (T--) {
    a = read_uint();
    b = read_uint();
    printf("%d\n", a - 1);
    while (b--)
      while (getchar_unlocked() != '\n');
  }
  return 0;
}


