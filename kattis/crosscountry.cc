#include <stdio.h>

#include <functional>
#include <queue>
#include <tuple>
#include <vector>

using namespace std;

int ReadInt() {
  int o = 0;
  char c = getchar_unlocked();
  while ('0' <= c && c <= '9') {
    o = (o * 10) + (c - '0');
    c = getchar_unlocked();
  }
  return o;
}

int Dijkstra(int N, const vector<vector<int>> &grid, int S, int T) {
  priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
  int d, u;
  vector<int> min_dist(N, 100000);
  min_dist[S] = 0;
  pq.emplace(0, S);
  while (!pq.empty()) {
    tie(d, u) = pq.top();
    pq.pop();
    if (min_dist[u] < d) continue;
    if (u == T) return d;
    for (int v = 0; v < N; ++v) {
      if (grid[u][v] + d >= min_dist[v]) continue;
      min_dist[v] = grid[u][v] + d;
      pq.emplace(grid[u][v] + d, v);
    }
  }
  return -1;
}

int main() {
  int N, S, T;
  scanf("%d %d %d\n", &N, &S, &T);
  vector<vector<int>> grid(N, vector<int>(N, -1));
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      grid[i][j] = ReadInt();
    }
  }
  printf("%d\n", Dijkstra(N, grid, S, T));
}

