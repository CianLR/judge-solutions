#include <math.h>
#include <stdio.h>

#include <string>
#include <vector>

using namespace std;

typedef vector<string> ColourList;

static double EPS = 1e-9;

static double Dist(double ax, double ay,
                   double bx, double by) {
  return sqrt(pow(ax - bx, 2) + pow(ay - by, 2));
}

struct Drop {
  Drop(int col, double r_, double x_, double y_)
   : colour(col), r(r_), x(x_), y(y_) {}

  void Print() const {
    printf("Drop colour %d, at (%lf, %lf) with rad %lf\n",
           colour, x, y, r);
  }

  bool WithinRad(double nx, double ny) {
    return Dist(x, y, nx, ny) - r < EPS;
  }

  int colour;
  double r, x, y;
};

class Canvas {
 public:
  void AddDrop(const Drop &d) {
    drops_.push_back(d);
    // d.Print();
  }

  int GetColour(double x, double y) {
    int col = 0;
    for (unsigned int i = 0; i < drops_.size(); ++i) {
      if (drops_[i].WithinRad(x, y))
        col = drops_[i].colour;
    }
    return col;
  }

  void Clear() {
    drops_.clear();
  }

 private:
  vector<Drop> drops_;
};

double VolumeToRadius(double v) {
  return sqrt(v / M_PI);
}

int main() {
  int C, N, M;
  double X, Y, V;
  char col[21];
  ColourList cl;
  Canvas c;
  scanf("%d", &C);
  while (C--) {
    cl.emplace_back("white");
    scanf("%d", &N);
    for (int i = 1; i <= N; ++i) {
      scanf("%lf %lf %lf %s", &X, &Y, &V, (char *)&col);
      cl.emplace_back(col);
      c.AddDrop(Drop(i, VolumeToRadius(V), X, Y));
    }
    scanf("%d", &M);
    for (int i = 0; i < M; ++i) {
      scanf("%lf %lf", &X, &Y);
      printf("%s\n", cl[c.GetColour(X, Y)].c_str());
    }
    c.Clear();
    cl.clear();
  }
}

