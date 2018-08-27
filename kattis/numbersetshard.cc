#include <stdio.h>
#include <stdint.h>
#include <math.h>

#include <algorithm>
#include <vector>

using namespace std;

struct UF {
  UF(unsigned int N) : parent(N, -1), size(N, 1), sets(N) {
    for (unsigned int i = 0; i < N; ++i) parent[i] = i;
  }

  int Root(unsigned int a) {
    while (parent[a] != a) {
      parent[a] = parent[parent[a]];
      a = parent[a];
    }
    return a;
  }

  void Join(unsigned int a, unsigned int b) {
    a = Root(a);
    b = Root(b);
    if (a == b) return;
    if (size[a] > size[b]) {
      parent[b] = a;
      size[a] += size[b];
    } else {
      parent[a] = b;
      size[b] += size[a];
    }
    --sets;
  }

  vector<unsigned int> parent;
  vector<unsigned int> size;
  unsigned int sets;
};

void SieveEroth(int N, vector<int> &primes) {
  primes.push_back(2);
  vector<bool> is_prime(N, true);
  double sqrt_n = sqrt(N);
  for (unsigned int p = 3; p < N; p += 2) {
    if (!is_prime[p]) continue;
    primes.push_back(p);
    if (p >= sqrt_n) continue;
    for (unsigned int p2 = p * p; p2 < N; p2 += p * 2) {
      is_prime[p2] = false;
    }
  }
}

vector<int> PRIMES;

inline uint64_t LowestGTMul(uint64_t lo, int m) {
  uint64_t x = lo / m;
  if (x * m == lo) return x * m;
  return (x + 1) * m;
}

int main() {
  SieveEroth(1000001, PRIMES);
  int C;
  uint64_t a, b, p;
  scanf("%d", &C);
  for (int c = 1; c <= C; ++c) {
    scanf("%lu %lu %lu", &a, &b, &p);
    UF uf((b - a) + 1);
    auto it = lower_bound(PRIMES.begin(), PRIMES.end(), p);
    for (; it != PRIMES.end(); ++it) {
      uint64_t start = LowestGTMul(a, *it);
      for (uint64_t nxt = start + *it; nxt <= b; nxt += *it) {
        uf.Join(start - a, nxt - a);
      }
    }
    printf("Case #%d: %u\n", c, uf.sets);
  }
}

