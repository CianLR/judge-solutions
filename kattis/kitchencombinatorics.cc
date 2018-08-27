#include <stdio.h>
#include <stdint.h>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

inline bool comb_works(unordered_map<int, unordered_set<int>> &incomps,
                       const int &s, const int &m, const int &d) {
  return incomps[s].count(m) == 0 and
         incomps[s].count(d) == 0 and
         incomps[m].count(d) == 0;
}

int main() {
  int R, S, M, D, N, k, x;
  scanf("%d %d %d %d %d", &R, &S, &M, &D, &N);
  vector<int> ingr_brands(R);
  for (int i = 0; i < R; ++i)
    scanf("%d", &ingr_brands[i]);

  vector<unordered_set<int>> dishes(S + M + D);
  for (unsigned int i = 0; i < dishes.size(); ++i) {
    scanf("%d", &k);
    dishes[i].reserve(k);
    for (int j = 0; j < k; ++j) {
      scanf("%d", &x);
      dishes[i].insert(x - 1);
    }
  }

  unordered_map<int, unordered_set<int>> incomps;
  for (int i = 0; i < N; ++i) {
    scanf("%d %d", &k, &x);
    incomps[k - 1].insert(x - 1);
    incomps[x - 1].insert(k - 1);
  }

  unsigned __int128 c, combs = 0;
  unordered_set<int> ingredient_types;
  for (int s = 0; s < S; ++s) {
    for (int m = S; m < S + M; ++m) {
      for (int d = S + M; d < S + M + D; ++d) {
        if (!comb_works(incomps, s, m, d))
          continue;
        ingredient_types.clear();
        ingredient_types.insert(dishes[s].begin(), dishes[s].end());
        ingredient_types.insert(dishes[m].begin(), dishes[m].end());
        ingredient_types.insert(dishes[d].begin(), dishes[d].end());
        c = 1;
        for (auto &in : ingredient_types) {
          c *= ingr_brands[in];
        }
        combs += c;
        if (combs > 1000000000000000000) {
          printf("too many\n");
          return 0;
        }
      }
    }
  }
  printf("%llu\n", (unsigned long long)combs);
  return 0;
}

