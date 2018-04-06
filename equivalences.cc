#include <stdio.h>
#include <stack>
#include <vector>

using namespace std;

typedef vector<vector<int>> AdjMatrix;

void DFS(const AdjMatrix &adj, int u, vector<bool> &visited, stack<int> &s) {
  visited[u] = true;
  for (auto const &v : adj[u]) {
    if (!visited[v]) DFS(adj, v, visited, s);
  }
  s.push(u);
}

void KosarajuSCC(int N, const AdjMatrix &adj, const AdjMatrix &adj_rev, AdjMatrix &scc_graph) {
  stack<int> s, scc;
  vector<bool> visited(N, false);
  for (int u = 0; u < N; ++u) {
    if (visited[u]) continue;
    DFS(adj, u, visited, s);
  }
  visited.assign(N, false);
  vector<int> scc_id(N, -1);
  vector<vector<int>> sccs;
  while (!s.empty()) {
    int u = s.top();
    s.pop();
    if (visited[u]) continue;
    DFS(adj_rev, u, visited, scc);
    sccs.emplace_back();
    while (!scc.empty()) {
      sccs.back().push_back(scc.top());
      scc_id[scc.top()] = sccs.size() - 1;
      scc.pop();
    }
  }
  scc_graph.resize(sccs.size());
  for (size_t i = 0; i < sccs.size(); ++i) {
    for (auto const &u : sccs[i]) {
      for (auto const &v : adj[u]) {
        if (i != scc_id[v])
          scc_graph[i].push_back(scc_id[v]);
      }
    }
  }
}

int GetMinSCCEdges(int N, const AdjMatrix &adj) {
  if (N == 1) return 0;
  int no_out_edges = 0, no_in_edges = 0;
  vector<bool> in_edges(N, false);
  for (int u = 0; u < N; ++u) {
    if (adj[u].empty()) ++no_out_edges;
    for (auto const &v : adj[u]) {
      in_edges[v] = true;
    }
  }
  for (int i = 0; i < N; ++i)
    if (!in_edges[i]) ++no_in_edges;
  return no_in_edges > no_out_edges ? no_in_edges : no_out_edges;
}

int main() {
  int T, N, M, u, v;
  scanf("%d", &T);
  while (T--) {
    scanf("%d %d", &N, &M);
    AdjMatrix adj(N), adj_rev(N), scc_graph;
    for (int i = 0; i < M; ++i) {
      scanf("%d %d", &u, &v);
      adj[u - 1].push_back(v - 1);
      adj_rev[v - 1].push_back(u - 1);
    }
    KosarajuSCC(N, adj, adj_rev, scc_graph);
    printf("%d\n", GetMinSCCEdges(scc_graph.size(), scc_graph));
  }
}
