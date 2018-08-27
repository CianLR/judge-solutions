#include <stdio.h>
#include <stdlib.h>

using namespace std;

unsigned int get_int() {
  unsigned int i = 0;
  char c = getchar_unlocked();
  while (c <= '9' && c >= '0') {
    i = (i * 10) + c - '0';
    c = getchar_unlocked();
  }
  return i;
}

void print_int(unsigned int i) {
  static char *str = static_cast<char *>(malloc(32));
  static char const digit[] = "0123456789";
  char *p = str;
  
  int shifter = i;
  do {
    ++p;
    shifter /= 10;
  } while (shifter);
  *p = '\0';

  do {
    *--p = digit[i % 10];
    i /= 10;
  } while (i);

  while (*p) putchar_unlocked(*p++);
}

int main() {
  unsigned int g, N = get_int(), last = get_int();
  unsigned int *gis = static_cast<unsigned int *>(malloc(N * sizeof(unsigned int)));
  unsigned int *gis_p = gis;
  
  *++gis_p = last;

  while (--N) {
    g = get_int();
    if (g > last) {
      *++gis_p = g;
      last = g;
    }
  }

  print_int(gis_p - gis);
  putchar_unlocked('\n');
  while (gis != gis_p) {
    print_int(*++gis);
    putchar_unlocked(' ');
  }
  putchar_unlocked('\n');
}

