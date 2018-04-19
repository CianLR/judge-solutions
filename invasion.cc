#include <stdio.h>

#include <functional>
#include <queue>
#include <tuple>
#include <utility>
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

struct Edge {
  Edge(int v_, int w_) : v(v_), w(w_) {}
  int v, w;
};

int Dijkstra(int N, int K, const vector<vector<Edge>> &adj, vector<int> &dist, int s) {
  int new_finds = dist[s] == -1, d, u;
  priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
  pq.emplace(0, s);
  dist[s] = 0;
  while (!pq.empty()) {
    tie(d, u) = pq.top(); pq.pop();
    if (dist[u] < d) continue;
    for (const auto &e : adj[u]) {
      if (d + e.w < K && (dist[e.v] == -1 || dist[e.v] > d + e.w)) {
        if (dist[e.v] == -1) ++new_finds;
        dist[e.v] = d + e.w;
        pq.emplace(d + e.w, e.v);
      }
    }
  }
  return new_finds;
}

int main() {
  int N, M, A, K, a, b, d;
  while (scanf("%d %d %d %d\n", &N, &M, &A, &K), N) {
    vector<vector<Edge>> adj(N);
    for (int i = 0; i < M; ++i) {
      a = ReadInt(), b = ReadInt(), d = ReadInt();
      adj[a - 1].emplace_back(b - 1, d);
      adj[b - 1].emplace_back(a - 1, d);
    }
    vector<int> bases(A, -1);
    for (int i = 0; i < A; ++i)
      bases[i] = ReadInt();
    // Count captures.
    int captures = 0;
    vector<int> dists(N, -1);
    for (int b = 0; b < A; ++b) {
      captures += Dijkstra(N, K, adj, dists, bases[b] - 1);
      printf("%d\n", N - captures);
    }
    putchar_unlocked('\n');
  }
}

