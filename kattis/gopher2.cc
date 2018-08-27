#include <stdio.h>
#include <complex>
#include <vector>

using namespace std;

vector<bool> visited(200, false);

bool dfs(const vector<vector<int>> &adj,
         vector<int> &right_pair,
         vector<int> &left_pair,
         int u) {
  visited[u] = true;
  for (auto &v : adj[u]) {
    if (left_pair[v] == -1 ||
        (!visited[left_pair[v]] && dfs(adj, right_pair, left_pair, left_pair[v]))) {
      left_pair[v] = u;
      right_pair[u] = v;
      return true;
    }
  }
  return false;
}

int kuhn(int N, int M, const vector<vector<int>> &adj) {
  vector<int> right_pair(N, -1), left_pair(M, -1);
  for (int i = 0; i < N; ++i) {
    if (right_pair[i] != -1) continue;  // Already paired.
    visited.assign(200, false);
    dfs(adj, right_pair, left_pair, i);
  }
  int unmatched = 0;
  for (int i = 0; i < N; ++i) {
    if (right_pair[i] == -1) ++unmatched;
  }
  return unmatched;
}

int main() {
  int N, M, S, V;
  double x, y;
  while (scanf("%d %d %d %d", &N, &M, &S, &V) == 4) {
    vector<complex<double>> gophers;
    for (int i = 0; i < N; ++i) {
      scanf("%lf %lf", &x, &y);
      gophers.emplace_back(x, y);
    }
    vector<complex<double>> holes;
    for (int i = 0; i < M; ++i) {
      scanf("%lf %lf", &x, &y);
      holes.emplace_back(x, y);
    }
    int max_dist = S * V;
    vector<vector<int>> adj(N);
    for (int u = 0; u < N; ++u) {
      for (int v = 0; v < M; ++v) {
        if (abs(gophers[u] - holes[v]) <= max_dist)
          adj[u].push_back(v);
      }
    }
    printf("%d\n", kuhn(N, M, adj));
  }
}

