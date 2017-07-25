
#include <cstdio>

using namespace std;

int main() {
  int T;
  scanf("%d", &T);
  while (T--) {
    int N;
    scanf("%d", &N);
    int curr_mod = 0;
    long long c;
    for (int i = 0; i < N; ++i) {
      scanf("%lld", &c);
      curr_mod += c % N;
      curr_mod %= N;
    }
    if (curr_mod == 0) {
      printf("YES\n");
    } else {
      printf("NO\n");
    }
  }
}

