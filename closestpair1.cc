#include <stdio.h>

#include <algorithm>
#include <complex>
#include <set>
#include <utility>
#include <vector>

using namespace std;

typedef complex<double> Point;

struct PointLtX {
  bool operator()(const Point &a, const Point &b) {
    if (real(a) < real(b)) {
      return true;
    }
    return real(a) == real(b) ? imag(a) < imag(b) : false;
  }
};

struct PointLtY {
  bool operator()(const Point &a, const Point &b) {
    if (imag(a) < imag(b)) {
      return true;
    }
    return imag(a) == imag(b) ? real(a) < real(b) : false;
  }
};

pair<Point, Point> ClosestPair(vector<Point> &points) {
  sort(points.begin(), points.end(), PointLtX());
  set<Point, PointLtY> cands;
  pair<Point, Point> closest;
  double min_dist = INFINITY;
  size_t last = 0;
  for (size_t front = 0; front < points.size(); ++front) {
    while (real(points[front]) - real(points[last]) >= min_dist && front > last) {
      cands.erase(points[last]);
      ++last;
    }
    double front_y = imag(points[front]);
    auto hi = cands.upper_bound(Point(INFINITY, front_y + min_dist));
    auto lo = cands.lower_bound(Point(INFINITY, front_y - min_dist));
    for (; lo != hi; ++lo) {
      double dst = abs(*lo - points[front]);
      if (dst < min_dist) {
        min_dist = dst;
        closest = pair<Point, Point>(*lo, points[front]);
      }
    }
    cands.insert(points[front]);
  }
  return closest;
}

int main() {
  int N;
  double x, y;
  vector<Point> points;
  while (scanf("%d", &N), N != 0) {
    for (int i = 0; i < N; ++i) {
      scanf("%lf %lf", &x, &y);
      points.emplace_back(x, y);
    }
    auto close = ClosestPair(points);
    printf("%lf %lf %lf %lf\n",
           real(close.first), imag(close.first),
           real(close.second), imag(close.second));
    points.clear();
  }
}

