#include <math.h>
#include <stdio.h>

#include <queue>
#include <vector>
#include <utility>
#include <functional>

using namespace std;

struct Point {
  Point(double x_=0, double y_=0)
    : x(x_), y(y_), in_tree(false) {}
  double x;
  double y;
  bool in_tree;
};

double dist(const Point &a, const Point &b) {
  return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

double prims_mst(int N, vector<Point> &pts) {
  typedef pair<double, Point *> CostPoint;
  priority_queue<
    CostPoint,
    vector<CostPoint>,
    greater<CostPoint>> pq;
  pq.emplace(0, &pts[0]);
  double cost = 0;
  int total_nodes = 0;
  while (total_nodes < N) {
    if (pq.top().second->in_tree) {
      pq.pop();
      continue;
    }
    cost += pq.top().first;
    ++total_nodes;
    Point *p = pq.top().second;
    //printf("Adding (%.02f, %.02f) at a cost of %.02f\n", p->x, p->y, pq.top().first);
    pq.pop();
    p->in_tree = true;
    for (int i = 0; i < N; ++i) {
      if (pts[i].in_tree)
        continue;
      pq.emplace(dist(*p, pts[i]), &pts[i]);
    }
  }
  return cost;
}

int main() {
  int T;
  scanf("%d\n\n", &T);
  while (T--) {
    int N;
    scanf("%d\n", &N);
    vector<Point> points(N);
    double tx, ty;
    for (int i = 0; i < N; ++i) {
      scanf("%lf %lf", &tx, &ty);
      points[i].x = tx;
      points[i].y = ty;
    }
    printf("%.02lf\n\n", prims_mst(N, points));
  }
}

