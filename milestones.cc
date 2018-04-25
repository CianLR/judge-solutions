#include <stdio.h>
#include <stdint.h>

#include <algorithm>
#include <unordered_set>
#include <vector>

using namespace std;

uint64_t GCD(uint64_t a, uint64_t b) {
  return b == 0 ? a : GCD(b, a % b);
}

vector<uint64_t> CalcPeriods(int N, const vector<uint64_t> &times) {
  vector<uint64_t> gaps(N - 1);
  for (int i = 0; i < N - 1; ++i)
    gaps[i] = times[i + 1] - times[i];
  uint64_t gcd = gaps[0];
  for (int i = 1; i < N - 1; ++i)
    gcd = GCD(gaps[i], gcd);
  for (int i = 0; i < N - 1; ++i)
    gaps[i] /= gcd;
  return gaps;
}

int main() {
  int N, M;
  scanf("%d %d\n", &M, &N);
  vector<uint64_t> times(M), stones(N);
  for (int i = 0; i < M; ++i)
    scanf("%lu", &times[i]);
  for (int i = 0; i < N; ++i)
    scanf("%lu", &stones[i]);

  vector<uint64_t> periods = CalcPeriods(M, times);

  unordered_set<uint64_t> dists;
  for (int start = 0; start <= N - M; ++start) {
    int stride = stones[start + 1] - stones[start];
    if (dists.find(stride / periods[0]) != dists.end()) continue;
    bool found = true;
    for (int p = start, i = 0; i < M - 1; ++p, ++i) {
      if ((stones[p + 1] - stones[p]) * periods[0] != stride * periods[i]) {
        found = false;
        break;
      }
    }
    if (found) dists.insert(stride / periods[0]);
  }
  vector<uint64_t> vecdists(dists.begin(), dists.end());
  sort(vecdists.begin(), vecdists.end());
  printf("%lu\n", vecdists.size());
  for (const auto &d : vecdists)
    printf("%lu ", d);
  putchar('\n');
}

