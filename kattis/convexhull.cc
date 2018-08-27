#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

struct Point {
  int x, y;
  bool operator<(const Point &b) {
    return x < b.x || (x == b.x && y < b.y);
  }
  bool operator==(const Point &b) {
    return x == b.x && y == b.y;
  }
};

inline bool Clockwise(const Point &a, const Point &b, const Point &c) {
  return (b.x - c.x) * (a.y - c.y) > (b.y - c.y) * (a.x - c.x);
}

inline bool CounterClockwise(const Point &a, const Point &b, const Point &c) {
  return (b.x - c.x) * (a.y - c.y) < (b.y - c.y) * (a.x - c.x);
}

void GetHull(const vector<Point> &points,
             bool (*cmp)(const Point &a, const Point &b, const Point &c),
             vector<Point> &hull) {
  for (auto &point : points) {
    while (hull.size() >= 2 && !cmp(hull.end()[-2], hull.end()[-1], point))
      hull.pop_back();
    hull.push_back(point);
  }
}

int main() {
  int N;
  while (scanf("%d", &N) && N != 0) {
    vector<Point> points(N), upper, lower;
    for (int i = 0; i < N; ++i)
      scanf("%d %d", &points[i].x, &points[i].y);
    sort(points.begin(), points.end());
    // Remove duplicates.
    points.resize(distance(points.begin(),
                           unique(points.begin(), points.end())));

    // Edge case, one unique point.
    if (points.size() == 1) {
      printf("1\n%d %d\n", points[0].x, points[0].y);
      continue;
    }
    
    GetHull(points, Clockwise, upper);
    GetHull(points, CounterClockwise, lower);
    
    printf("%lu\n", upper.size() + lower.size() - 2);
    for (auto point = upper.rbegin(); point != upper.rend() - 1; ++point) {
      printf("%d %d\n", point->x, point->y);
    }
    for (auto point = lower.begin(); point != lower.end() - 1; ++point) {
      printf("%d %d\n", point->x, point->y);
    }
  }
}

