#include <stdio.h>

#include <algorithm>
#include <tuple>
#include <vector>

using namespace std;

class UnionFind {
 public:
  UnionFind(int N) : root_(N, -1), size_(N, 1), clusters_(N) {
    for (int i = 0; i < N; ++i)
      root_[i] = i;
  }

  bool Connected(int a, int b) {
    return GetRoot(a) == GetRoot(b);
  }

  void Join(int a, int b) {
    int ar = GetRoot(a), br = GetRoot(b);
    if (ar == br) return;
    if (size_[br] > size_[ar]) root_[ar] = br, size_[br] += size_[ar];
    else                       root_[br] = ar, size_[ar] += size_[br];
    --clusters_;
  }

  int Clusters() {
    return clusters_;
  }

 private:
  vector<int> root_;
  vector<int> size_;
  int clusters_;

  int GetRoot(int a) {
    while (a != root_[a]) {
      root_[a] = root_[root_[a]];
      a = root_[a];
    }
    return a;
  }
};

void Kruskals(int N, const vector<tuple<int, int, int>> &edges,
              vector<int> &edges_used) {
  UnionFind uf(N);
  int ei = 0, d, u, v;
  while (uf.Clusters() > 1) {
    tie(d, u, v) = edges[ei++];
    if (uf.Connected(u, v)) continue;
    uf.Join(u, v);
    edges_used.push_back(ei - 1);
  }
}

int main() {
  int N, d;
  scanf("%d\n", &N);
  vector<tuple<int, int, int>> edges;
  for (int u = 0; u < N; ++u) {
    for (int v = 0; v < N; ++v) {
      scanf("%d", &d);
      if (v > u) edges.emplace_back(d, u, v);
    }
  }
  sort(edges.begin(), edges.end());
  vector<int> edges_used;
  Kruskals(N, edges, edges_used);
  for (auto &e : edges_used) {
    printf("%d %d\n", get<1>(edges[e]) + 1, get<2>(edges[e]) + 1);
  }
}

