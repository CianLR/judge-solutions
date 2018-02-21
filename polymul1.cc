#include <stdio.h>

#include <vector>

using namespace std;

void ReadPoly(vector<int> &poly) {
  int degree;
  scanf("%d", &degree);
  poly.resize(degree + 1);
  for (int i = 0; i <= degree; ++i) {
    scanf("%d", &poly[i]);
  }
}

void WritePoly(const vector<int> &poly) {
  printf("%lu\n", poly.size() - 1);
  for (unsigned int i = 0; i < poly.size(); ++i) {
    printf("%d ", poly[i]);
  }
  putchar('\n');
}

void MulPoly(const vector<int> &f, const vector<int> &s, vector<int> &o) {
  o.resize(f.size() + s.size() + 1);
  int largest = 0;
  for (unsigned int i = 0; i < f.size(); ++i) {
    for (unsigned int j = 0; j < s.size(); ++j) {
      o[i + j] += f[i] * s[j];
      largest = largest < i + j ? i + j : largest;
    }
  }
  o.resize(largest + 1);
}

int main() {
  int T, fd, sd;
  vector<int> first_poly, second_poly, out_poly;
  scanf("%d", &T);
  while (T--) {
    ReadPoly(first_poly);
    ReadPoly(second_poly);
    MulPoly(first_poly, second_poly, out_poly);
    WritePoly(out_poly);

    first_poly.clear();
    second_poly.clear();
    out_poly.clear();
  }
}

