#include <stdio.h>

#include <algorithm>
#include <queue>
#include <utility>
#include <tuple>
#include <vector>

using namespace std;

typedef vector<vector<pair<int, int>>> WeightAdj;

inline int Sq(int a) { return a * a; }

int SqPointDist(const pair<int, int> &a, const pair<int, int> &b) {
  return Sq(a.first - b.first) + Sq(a.second - b.second);
}

struct PairGT {
  bool operator()(const pair<int, int> &a, const pair<int, int> &b) {
    return a > b;
  }
};

void Dijkstra(int N, const WeightAdj &adj, int start, int end, vector<int> &path) {
  int s, u, v, d;
  priority_queue<pair<int, int>, vector<pair<int, int>>, PairGT> pq;
  pq.emplace(0, start);
  vector<int> best_dist(N, 1000000000);
  best_dist[start] = 0;
  vector<int> prev(N, -1);
  while (!pq.empty()) {
    tie(s, u) = pq.top(), pq.pop();
    if (best_dist[u] < s) continue;
    if (u == end) break;
    for (const auto &vd : adj[u]) {
      v = vd.first, d = vd.second;
      if (best_dist[v] <= s + d) continue;
      best_dist[v] = s + d;
      prev[v] = u;
      pq.emplace(s + d, v);
    }
  }
  int p = prev[end];
  while (prev[p] != -1) {
    path.push_back(p); 
    p = prev[p];
  }
  reverse(path.begin(), path.end());
}

int main() {
  int N, x, y, d;
  scanf("%d", &N);
  vector<pair<int, int>> shades;
  WeightAdj edges(N + 2);
  for (int u = 0; u < N + 2; ++u) {
    scanf("%d %d", &x, &y);
    shades.emplace_back(x, y);
    for (int v = 0; v < u; ++v) {
      d = SqPointDist(shades[v], shades[u]);
      edges[v].emplace_back(u, d);
      edges[u].emplace_back(v, d);
    }
  }

  vector<int> path;
  Dijkstra(N + 2, edges, N, N + 1, path);
  if (path.empty()) {
    printf("-\n");
  } else {
    for (size_t i = 0; i < path.size(); ++i)
      printf("%d\n", path[i]);
  }
}

