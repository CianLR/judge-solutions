#include <stdio.h>
#include <vector>
#include <utility>
#include <queue>
#include <functional>

using namespace std;

bool seen(const vector<vector<int>> &usage, const int &h, const int &w) {
  return usage[h][w] != -1;
}

bool seen(const vector<vector<int>> &usage, const pair<int, int> &coords) {
  return seen(usage, coords.first, coords.second);
}

#define MAX(a, b) ((a) > (b) ? (a) : (b))
const vector<pair<int, int>> dirs = {{1, 1}, {1, 0}, {1, -1}, {0, -1},
                                     {-1, -1}, {-1, 0}, {-1, 1}, {0, 1}};

int main() {
  //printf("hello\n");
  int H, W, DH, DW;
  scanf("%d %d", &H, &W);
  vector<vector<int>> sea(H, vector<int>(W, 0));
  for (int i = 0; i < H; ++i) {
    for (int j = 0; j < W; ++j) {
      scanf("%d", &sea[i][j]);
    }
  }
  scanf("%d %d", &DH, &DW);

  //printf("Declaring loop\n");
  vector<vector<int>> usage(H, vector<int>(W, -1));
  priority_queue<pair<int, pair<int, int>>> pq;
  pq.emplace(-sea[DH - 1][DW - 1], make_pair(DH - 1, DW - 1));
  unsigned long long drained = 0;
  //printf("Entering loop\n");
  while (!pq.empty()) {
    int dr = -pq.top().first;
    pair<int, int> coords = pq.top().second;
    pq.pop();
    //printf("At coord %d, %d\n", coords.first, coords.second);
    if (seen(usage, coords))
      continue;
    //printf("Draining %d, %d by %d\n", coords.first, coords.second, dr);
    drained += -dr;
    usage[coords.first][coords.second] = -dr;
    for (auto &d : dirs) {
      int a = coords.first + d.first, b = coords.second + d.second;
      if (0 <= a and a < H and 0 <= b and b < W and
          !seen(usage, a, b) and sea[a][b] < 0) {
        int mx = MAX(dr, sea[a][b]);
        //printf("Adding %d, %d (%d) from %d %d (%d) with drain of %d\n",
        //       a, b, sea[a][b], coords.first, coords.second, dr, mx);
        pq.emplace(-mx, make_pair(a, b));
      }
    }
  }
  printf("%llu\n", drained);
}

