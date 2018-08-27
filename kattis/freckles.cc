#include <queue>
#include <unordered_map>
#include <vector>
#include <utility>
#include <functional>

#include <stdio.h>
#include <math.h>

using namespace std;

struct UnionFind {
  int GetRoot(int a) {
    if (parent.find(a) == parent.end()) {
      parent[a] = a;
      size[a] = 1;
    }
    while (parent[a] != a) {
      a = parent[a];
    }
    return a;
  }

  void Union(int a, int b) {
    int ar = GetRoot(a), br = GetRoot(b);
    if (ar == br)
      return;
    if (size[ar] > size[br]) {
      parent[br] = ar;
      size[ar] += size[br];
    } else {
      parent[ar] = br;
      size[br] += size[ar];
    }
  }

  bool IsJoined(int a, int b) {
    return GetRoot(a) == GetRoot(b);
  }

  unordered_map<int, int> parent;
  unordered_map<int, int> size;
};

struct Point {
  Point(double x_=0.0, double y_=0.0) : x(x_), y(y_) {}
  double x;
  double y;
};

double dist(const Point &p1, const Point &p2) {
  return sqrt(pow(p1.x - p2.x, 2) + pow(p1.y - p2.y, 2));
}

typedef pair<double, pair<int, int> > WeightedEdge;

int main() {
  int T, N;
  double x, y;
  scanf("%d\n\n", &T);
  while (T--) {
    scanf("%d\n", &N);
    vector<Point> pts(N);
    priority_queue<
      WeightedEdge,
      vector<WeightedEdge>,
      greater<WeightedEdge> > pq;
    for (int i = 0; i < N; ++i) {
      scanf("%lf %lf", &x, &y);
      pts[i].x = x;
      pts[i].y = y;
      for (int j = 0; j < i; ++j) {
        double weight = dist(pts[i], pts[j]);
        pq.emplace(weight, pair<int, int>(i, j));
      }
    }

    UnionFind uf;
    double cost = 0.0;
    int edges_used = 0;
    WeightedEdge e;
    while (edges_used < N - 1) {
      e = pq.top();
      pq.pop();
      if (uf.IsJoined(e.second.first, e.second.second))
        continue;
      ++edges_used;
      cost += e.first;
      uf.Union(e.second.first, e.second.second);
    }
    printf("%.02lf\n\n", cost);
  }
}


