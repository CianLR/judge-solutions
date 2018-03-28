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
  int matched = 0;
  for (int i = 0; i < N; ++i) {
    if (right_pair[i] != -1) ++matched;
  }
  return matched;
}

typedef vector<complex<double>> PointVec;

int escapes(int M, int N, const PointVec &robots, const PointVec &holes, int dist) {
  vector<vector<int>> adj(M);
  for (int r = 0; r < M; ++r) {
    for (int h = 0; h < N; ++h) {
      if (abs(robots[r] - holes[h]) <= dist) {
        adj[r].push_back(h);
      }
    }
  }
  return kuhn(M, N, adj);
}

int main() {
  int M, N, scenario=1;
  vector<int> times = {5, 10, 20};
  const int speed = 10;  // m/s
  double x, y;
  while (scanf("%d", &M), M != 0) {
    PointVec robots, holes;
    for (int i = 0; i < M; ++i) {
      scanf("%lf %lf", &x, &y);
      robots.emplace_back(x, y);
    }
    scanf("%d", &N);
    for (int i = 0; i < N; ++i) {
      scanf("%lf %lf", &x, &y);
      holes.emplace_back(x, y);
    }
    printf("Scenario %d\n", scenario++);
    for (auto &time : times) {
      printf("In %d seconds %d robot(s) can escape\n",
             time, escapes(M, N, robots, holes, time * speed));
    }
    putchar('\n');
  }
}

