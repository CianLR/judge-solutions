#include <stdio.h>
#include <vector>

using namespace std;

struct Object {
  Object(int i_, int v, int w) : i(i_), value(v), weight(w) {}
  int i, value, weight;
};

void knapsack(int cap, const vector<Object> &objs, vector<int> &taken_inds) {
  vector<vector<int>> values(objs.size() + 1, vector<int>(cap + 1, 0));
  vector<vector<bool>> taken(objs.size(), vector<bool>(cap + 1, false));
  for (auto &item : objs) {
    for (int c = 0; c <= cap; ++c) {
      if (c < item.weight ||
          values[item.i][c - item.weight] + item.value < values[item.i][c]) {
        values[item.i + 1][c] = values[item.i][c];
      } else {
        values[item.i + 1][c] = values[item.i][c - item.weight] + item.value;
        taken[item.i][c] = true;
      }
    }
  }

  int c = cap;
  for (int i = objs.size() - 1; i >= 0; --i) {
    if (taken[i][c]) {
      taken_inds.push_back(i);
      c -= objs[i].weight;
    }
  }
}

int main() {
  float C;
  int N, v, w;
  while (scanf("%f %d", &C, &N) == 2) {
    vector<Object> objs;
    for (int i = 0; i < N; ++i) {
      scanf("%d %d", &v, &w);
      objs.emplace_back(i, v, w);
    }

    vector<int> taken;
    knapsack((int)C, objs, taken);
    
    printf("%lu\n", taken.size());
    for (size_t i = 0; i < taken.size(); ++i)
      printf("%d ", taken[i]);
    printf("\n");
  }
}

