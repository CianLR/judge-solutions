#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

#define MAXS 10e5

vector<long long> color;

int main() {
  int S, C;
  long long K;
  scanf("%d %d %lld", &S, &C, &K);
  color.assign(S, -1);
  for (int i = 0; i < S; ++i)
    scanf("%lld", &color[i]);
  sort(color.begin(), color.end());

  int machines = 1, cur_sz = 0, start_col = color[0];
  for (int i = 0; i < S; ++i) {
    if (color[i] - start_col > K or cur_sz == C) {
      machines += 1;
      start_col = color[i];
      cur_sz = 0;
    }
    cur_sz += 1;
  }

  printf("%d\n", machines);
}

