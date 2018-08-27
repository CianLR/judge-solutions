#include <cstdio>
#include <cstring>

bool go_up[40][1001];
int memo[40][1001];
int dists[40];
int N;

const int kImpossible = 10000;

int climb(int i, int h) {
  if (i == N) return h == 0 ? 0 : kImpossible;
  if (memo[i][h] != -1) return memo[i][h];
  int dist_up = climb(i + 1, h + dists[i]),
      dist_dn = kImpossible;
  if (h - dists[i] >= 0)
    dist_dn = climb(i + 1, h - dists[i]);
  if (dist_up < dist_dn) {
    go_up[i][h] = true;
    memo[i][h] = dist_up;
  } else {
    go_up[i][h] = false;
    memo[i][h] = h > dist_dn ? h : dist_dn;
  }
  return memo[i][h];
}

int main() {
  int T;
  scanf("%d\n", &T);
  while (T--) {
    scanf("%d\n", &N);
    memset(memo, -1, sizeof(memo));
    for (int i = 0; i < N;++i)
      scanf("%d", &dists[i]);
    int cl = climb(0, 0);
    if (cl == kImpossible) {
      printf("IMPOSSIBLE\n");
    } else {
      int h = 0;
      for (int i = 0; i < N;++i) {
        putchar(go_up[i][h] ? 'U' : 'D');
        h += go_up[i][h] ? dists[i] : -dists[i];;
      }
      putchar('\n');
    }
  }
}

