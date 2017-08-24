#include <stdio.h>

#include <vector>
#include <unordered_set>

using namespace std;

typedef vector<unordered_set<int>> AdjList;

const int COLOURS = 4;

bool check_safe(int node, const AdjList &lst, const vector<int> &colours, int c) {
  for (auto it = lst[node].begin(); it != lst[node].end(); ++it) {
    if (colours[*it] == c)
      return false;
  }
  return true;
}

bool colour(int node, const AdjList &lst, vector<int> &colours) {
  if (node >= lst.size())
    return true;
  for (int c = 0; c < COLOURS; ++c) {
    colours[node] = c;
    if (check_safe(node, lst, colours, c) && colour(node + 1, lst, colours))
      return true;
    colours[node] = -1;
  }
  return false;
}

int main() {
  int N;
  scanf("%d", &N);
  AdjList lst(N);
  int a, b;
  while (scanf("%d-%d", &a, &b) >= 0) {
    lst[a - 1].insert(b - 1);
    lst[b - 1].insert(a - 1);
  }
  vector<int> colours(N, -1);
  if (!colour(0, lst, colours)) {
    return 1;
  }
  for (int i = 0; i < N; ++i) {
    printf("%d %d\n", i + 1, colours[i] + 1);
  }
}

