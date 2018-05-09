#include <stdio.h>

#include <queue>
#include <vector>

using namespace std;

struct Edge {
  Edge(int u_, int v_, int c_) : u(u_), v(v_), c(c_), f(0) {}
  int Other(int k) {
    return k == u ? v : u;
  }
  int CapTo(int k) {
    return k == v ? c - f : f;
  }
  void AddFlowTo(int k, int flow) {
    if (k == v) f += flow;
    else        f -= flow;
  }
  int u, v, c, f;
};

typedef vector<vector<Edge *>> Graph;

bool BFSLevels(int N, const Graph &graph, int s, int t, vector<int> &levels) {
  levels.assign(N, -1);
  queue<int> q;
  q.push(s);
  levels[s] = 0;
  while (!q.empty()) {
    int u = q.front(); q.pop();
    for (auto &e : graph[u]) {
      int v = e->Other(u);
      if (levels[v] == -1 && e->CapTo(v) > 0) {
        levels[v] = levels[u] + 1;
        q.push(v);
      }
    }
  }
  return levels[t] != -1;
}

int Augment(int N, Graph &graph, int u, int t, const vector<int> &levels, int flow) {
  if (u == t) return flow;
  int f = 0;
  auto e = graph[u].begin();
  for (; e != graph[u].end(); ++e) {
    int v = (*e)->Other(u), cap = (*e)->CapTo(v);
    if (cap == 0 || levels[v] != levels[u] + 1) continue;
    f = Augment(N, graph, v, t, levels, flow < cap ? flow : cap);
    if (f > 0) {
      (*e)->AddFlowTo(v, f);
      break;
    }
  }
  graph[u].erase(graph[u].begin(), e);
  return f;
}

vector<int> Dinics(int N, const Graph &graph, int s, int t) {
  vector<int> levels;
  while (BFSLevels(N, graph, s, t, levels)) {
    Graph curr_graph = graph;
    while (Augment(N, curr_graph, s, t, levels, 100000000) > 0);
  }
  vector<int> U;
  for (int i = 0; i < N; ++i)
    if (levels[i] != -1) U.push_back(i);
  return U;
}

int main() {
  int N, M, S, T, u, v, c;
  scanf("%d %d %d %d\n", &N, &M, &S, &T);
  Edge *edges[M];
  Graph graph(N);
  for (int i = 0; i < M; ++i) {
    scanf("%d %d %d", &u, &v, &c);
    edges[i] = new Edge(u, v, c);
    graph[u].push_back(edges[i]);
    graph[v].push_back(edges[i]);
  }
  vector<int> U = Dinics(N, graph, S, T);
  printf("%lu\n", U.size());
  for (auto &k : U) printf("%d\n", k);
}
