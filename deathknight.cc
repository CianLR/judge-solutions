#include <stdio.h>

int main() {
  int N;
  scanf("%d", &N);
  char battle[1001];
  int won = N;
  while (N--) {
    scanf("%s\n", battle);
    int i = 0;
    while (battle[++i]) {
      if (battle[i] == 'D' && battle[i - 1] == 'C') {
        --won;
        break;
      }
    }
  }
  printf("%d\n", won);
}

