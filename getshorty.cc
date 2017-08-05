#include <cstdio>
#include <queue>
#include <vector>
#include <utility>
#include <functional>

using namespace std;

int main() {
  int N, M;
  while (scanf("%d %d", &N, &M) && M != 0 && N != 0) {
    vector<vector<pair<int, float>>> adj(N);
    int u, v;
    float c;
    for (int i = 0; i < M; ++i) {
      scanf("%d %d %f", &u, &v, &c);
      adj[u].push_back(make_pair(v, c));
      adj[v].push_back(make_pair(u, c));
    }
    vector<float> dist(N, -1);
    priority_queue<pair<float, int>, vector<pair<float, int>>, less<pair<float, int>>> pq;
    //dist[0] = 1;
    pq.push(make_pair(1, 0));
    while (!pq.empty()) {
      int curr = pq.top().second;
      float cost = pq.top().first;
      pq.pop();
      if (dist[curr] != -1)
        continue;
      dist[curr] = cost;
      if (curr == N - 1)
        break;
      for (unsigned int i = 0; i < adj[curr].size(); ++i) {
        if (dist[adj[curr][i].first] == -1) {
          pq.push(make_pair(cost * adj[curr][i].second, adj[curr][i].first));
        }
      }
    }
    printf("%.4f\n", dist[N - 1]);
  }
  return 0;
}

