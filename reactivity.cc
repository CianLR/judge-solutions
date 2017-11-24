#include <stdio.h>
#include <vector>

using namespace std;

#define MAXN 1000

vector<vector<int>> deps(MAXN);
vector<int> satisfy_deps(MAXN);

int main() {
  int N, K, a, b;
  scanf("%d %d", &N, &K);
  for (int i = 0; i < K; ++i) {
    scanf("%d %d", &a, &b);
    deps[a].push_back(b);
    satisfy_deps[b] += 1;
  }
  
  int next_node = -1;
  for (int i = 0; i < N; ++i) {
    if (satisfy_deps[i] == 0) {
      if (next_node != -1) {
        printf("back to the lab\n");
        return 0;
      }
      next_node = i;
    }
  }

  vector<int> series;
  while (next_node != -1) {
    series.push_back(next_node);
    auto &next_deps = deps[next_node];
    next_node = -1;
    for (auto &v : next_deps) {
      satisfy_deps[v] -= 1;
      if (satisfy_deps[v] == 0) {
        if (next_node != -1) {
          printf("back to the lab\n");
          return 0;
        }
        next_node = v;
      }
    }
  }
  
  for (auto &n : series) {
    printf("%d ", n);
  }
  printf("\n");
  return 0;
}

