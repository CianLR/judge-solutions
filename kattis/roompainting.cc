#include <algorithm>
#include <vector>

#include <stdio.h>

using namespace std;

unsigned long long read_ull() {
  unsigned long long i = 0;
  char c = getchar_unlocked();
  while (c < 58 && c > 47) {
    i = (i * 10) + (c - 48);
    c = getchar_unlocked();
  }
  return i;
}

int main() {
  unsigned long long N = read_ull(), M = read_ull(), c;

  vector<unsigned long long> cans(N);
  for (int i = 0; i < N; ++i) {
    cans[i] = read_ull();
  }
  sort(cans.begin(), cans.end());

  vector<unsigned long long> needed(M);
  for (int i = 0; i < M; ++i) {
    needed[i] = read_ull();
  }
  sort(needed.begin(), needed.end());

  unsigned long long waste = 0;
  auto it_begin = cans.begin();
  for (int i = 0; i < needed.size(); ++i) {
    it_begin = lower_bound(it_begin, cans.end(), needed[i]);
    waste += *it_begin - needed[i];
  }
  printf("%lld\n", waste);
}

