#include <math.h>
#include <stdio.h>

#define MAX(a, b) ((a) < (b) ? (b) : (a))

class PriceCalc {
 public:
  PriceCalc(int p, int a, int b, int c, int d)
   : p_(p), a_(a), b_(b), c_(c), d_(d) {}

  double Price(int k) {
    return p_ * (sin(a_ * k + b_) + cos(c_ * k + d_) + 2);
  }

 private:
  const int p_, a_, b_, c_, d_;

};

int main() {
  int p, a, b, c, d, n;
  scanf("%d %d %d %d %d %d", &p, &a, &b, &c, &d, &n);
  PriceCalc pc(p, a, b, c, d);

  double pr, top = pc.Price(1), drop = 0;
  for (int i = 2; i <= n; ++i) {
    pr = pc.Price(i);
    if (pr > top) top = pr;
    else drop = MAX(drop, top - pr);
  }
  printf("%lf\n", drop);
}

