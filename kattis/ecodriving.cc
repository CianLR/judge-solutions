#include <stdio.h>
#include <math.h>

#include <complex>
#include <functional>
#include <tuple>
#include <queue>
#include <vector>
#include <unordered_map>
#include <utility>

using namespace std;

#define ERROR_ANGLE 420.0
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))

struct Node {
  Node(int i_, complex<double> point_)
    : i(i_), point(point_) {}

  int i;
  complex<double> point;
  vector<Node *> adj;
};

double node_dist(const Node *a, const Node *b) {
  return abs(b->point - a->point);
}

double node_angle(const Node *a, const Node *b) {
  return arg(b->point - a->point);
}

double angle_diff(double a, double b) {
  if (a == ERROR_ANGLE || b == ERROR_ANGLE) return 0;
  return MIN((M_PI * 2) - abs(a - b), abs(a - b));
}

typedef tuple<double, double, double, Node *, Node *> TraverseStep;

double TraverseGraph(Node *start, Node *end, int V, int max_dist) {
  double max_angle, dist, direc;
  Node *u, *v, *p;
  priority_queue<TraverseStep,
                 vector<TraverseStep>,
                 greater<TraverseStep>> pq;
  vector<vector<double>> dist_maps(V, vector<double>(V, INFINITY));
  pq.emplace(0, 0, ERROR_ANGLE, start, start);
  while (!pq.empty()) {
    tie(max_angle, dist, direc, u, p) = pq.top();
    dist_maps[p->i][u->i] = dist;
    // printf("At %d, dist %lf, max_angle %lf\n",
    //        u->i, dist, max_angle * 180 / M_PI);
    pq.pop();
    if (u->i == end->i) return max_angle;
    for (size_t i = 0; i < u->adj.size(); ++i) {
      v = u->adj[i];
      double new_dist = dist + node_dist(u, v);
      double new_direc = node_angle(u, v);
      double diff = angle_diff(direc, new_direc);
      // printf("Adding %d -> %d\n", u->i, v->i);
      if (dist_maps[u->i][v->i] < new_dist || new_dist > max_dist) {
        // printf("nvm\n");
        continue; 
      }
      pq.emplace(MAX(max_angle, diff), new_dist, new_direc, v, u);
    }
  }
  return ERROR_ANGLE;
}

int main() {
  int J, R, D, x, y;
  scanf("%d %d %d", &J, &R, &D);
  vector<Node> nodes;
  for (int i = 0; i < J; ++i) {
    scanf("%d %d", &x, &y);
    nodes.emplace_back(i, complex<double>(x, y));
  }
  for (int i = 0; i < R; ++i) {
    scanf("%d %d", &x, &y);
    nodes[x - 1].adj.push_back(&nodes[y - 1]);
  }

  double angle = TraverseGraph(&nodes.front(), &nodes.back(), J, D);
  if (angle == ERROR_ANGLE) {
    printf("Impossible\n");
    return 0;
  }
  printf("%lf\n", angle * 180 / M_PI);
}

