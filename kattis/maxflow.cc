#include <stdio.h>
#include <limits.h>

#include <queue>
#include <vector>

using namespace std;

struct Edge {
  Edge(int u_ = -1, int v_ = -1, int mx_ = -1) : u(u_), v(v_), mx(mx_), f(0) {}
  // From, to, maxflow, flow.
  int CapacityTo(int k) const {
    return k == v ? mx - f : f;
  }
  void AddFlowTo(int k, int flow) {
    if (k == v) f += flow;
    else        f -= flow;
  }
  int Other(int k) const {
    return k == u ? v : u;
  }
  int u, v, mx, f;
};

typedef vector<vector<Edge *>> Graph;

bool BFSLevel(int N, const Graph &graph, int s, int t, vector<int> &levels) {
  levels.assign(N, -1);
  queue<int> q;
  q.push(s);
  levels[s] = 0;
  while (!q.empty()) {
    int u = q.front();
    q.pop();
    for (const auto &e : graph[u]) {
      int v = e->Other(u);
      if (levels[v] != -1 || e->CapacityTo(v) == 0) continue;
      levels[v] = levels[u] + 1;
      q.push(v);
    }
  }
  return levels[t] != -1;
}

int DFSAddFlow(int N, Graph &graph, const vector<int> &levels, int t, int u, int flow) {
  if (u == t) return flow;
  for (auto e = graph[u].begin(); e != graph[u].end(); ++e) {
    int v = (*e)->Other(u), edge_flow = (*e)->CapacityTo(v);
    if (levels[v] != levels[u] + 1 || edge_flow == 0) continue;
    edge_flow = DFSAddFlow(N, graph, levels, t, v,
                           edge_flow < flow ? edge_flow : flow);
    if (edge_flow > 0) {
      (*e)->AddFlowTo(v, edge_flow);
      graph[u].erase(graph[u].begin(), e);
      return edge_flow;
    }
  }
  graph[u].clear();
  return 0;
}

int EdmondsKarp(int N, Graph &graph, int s, int t) {
  int flow = 0, path_flow;
  vector<int> levels;
  while (BFSLevel(N, graph, s, t, levels)) {
    Graph cur_graph = graph;
    while ((path_flow = DFSAddFlow(N, cur_graph, levels, t, s, INT_MAX)) > 0)
      flow += path_flow;
  }
  return flow;
}

int main() {
  int N, M, S, T, u, v, c;
  scanf("%d %d %d %d", &N, &M, &S, &T);
  Graph graph(N);
  Edge *edges = new Edge[M];
  for (int i = 0; i < M; ++i ) {
    scanf("%d %d %d", &u, &v, &c);
    edges[i] = Edge(u, v, c);
    graph[u].push_back(&edges[i]);
    graph[v].push_back(&edges[i]);
  }
  int flow = EdmondsKarp(N, graph, S, T);
  int used_edges = 0;
  for (int i = 0; i < M; ++i) {
    if (edges[i].f > 0) ++used_edges;
  }
  printf("%d %d %d\n", N, flow, used_edges);
  for (int i = 0; i < M; ++i) {
    if (edges[i].f > 0)
      printf("%d %d %d\n", edges[i].u, edges[i].v, edges[i].f);
  }
}

