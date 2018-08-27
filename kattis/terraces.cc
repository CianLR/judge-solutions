#include <stdio.h>

#include <deque>
#include <tuple>
#include <utility>
#include <vector>

using namespace std;

const vector<pair<int, int>> DIRS = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

int BFS(int H, int W,
        const vector<vector<int>> &grid,
        vector<vector<bool>> &visited,
        int sh, int sw) {
  int h, w, depth = grid[sh][sw], count = 1;
  bool has_sink = false;
  deque<pair<int, int>> q;
  visited[sh][sw] = true;
  q.emplace_back(sh, sw);
  while (!q.empty()) {
    tie(h, w) = q.front();
    q.pop_front();
    for (const auto &d : DIRS) {
      int nh = h + d.first, nw = w + d.second;
      if (nh < 0 || nh >= H || nw < 0 || nw >= W) continue;
      if (grid[nh][nw] < depth) {
        has_sink = true;
      } else if (grid[nh][nw] == depth && !visited[nh][nw]) {
        q.emplace_back(nh, nw);
        visited[nh][nw] = true;
        ++count;
      }
    }
  }
  if (has_sink) return 0;
  return count;
}

int main() {
  int W, H;
  scanf("%d %d\n", &W, &H);
  vector<vector<int>> grid(H, vector<int>(W));
  for (int h = 0; h < H; ++h)
    for (int w = 0; w < W; ++w)
      scanf("%d", &grid[h][w]);
  
  int flats = 0;
  vector<vector<bool>> visited(H, vector<bool>(W, false));
  for (int h = 0; h < H; ++h)
    for (int w = 0; w < W; ++w)
      if (!visited[h][w])
        flats += BFS(H, W, grid, visited, h, w);
  printf("%d\n", flats);
}

