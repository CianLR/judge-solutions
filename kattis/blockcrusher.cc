#include <cstdio>
#include <cstring>
#include <queue>
#include <vector>
#include <utility>
#include <functional>
#include <unordered_set>

#define gn(X, Y) (nodes[((Y)*W) + (X)] - 48)
#define gn_addr(X, Y) (&nodes[((Y)*W) + (X)])

#define compress(X, Y) (((Y)*W) + (X))
#define gpv(X, Y) (previous[((Y)*W) + (X)])
#define get_x(node) ((node) % W)
#define get_y(node) ((node) / W)

#define on_grid(X, Y) ((X) >= 0 && (Y) >= 0 && (X) < (W) && (Y) < H)

using namespace std;

#define cmb_p_c(p, c) (((p) << 16) + (c))
#define get_prev(x) (((x) & 0xFFFF0000) >> 16)
#define get_curr(x) ((x) & 0xFFFF)

#define is_end(node) ( ((node) / W) == H - 1)

int H, W;
char nodes[1200];
int previous[1200];
bool seen[1200];

int main() {
  while (scanf("%d %d", &H, &W) && H != 0) {
    memset(seen, 0, 1200);
    for (int i = 0; i < H; ++i)
      scanf("%s", gn_addr(0, i));
    
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    for (int i = 0; i < W; ++i) {
      pq.emplace(nodes[i] - 48, cmb_p_c(i, i));
    }
    int end = -1;
    while (!pq.empty()) {
      int cost = pq.top().first;
      int node = get_curr(pq.top().second);
      int prev_node = get_prev(pq.top().second);
      pq.pop();
      if (seen[node])
        continue;
      seen[node] = true;
      previous[node] = prev_node;
      // If we're on the final line then break.
      if (is_end(node)) {
        end = node;
        break;
      }
      // Otherwise add the edges
      int x = get_x(node);
      int y = get_y(node);
#define push_it(XMod, YMod) \
if (on_grid(x + XMod, y + YMod) && !seen[compress(x + XMod, y + YMod)]) \
  pq.emplace(cost + gn(x + XMod, y + YMod), cmb_p_c(node, compress(x + XMod, y + YMod)))
      push_it(1, 0);
      push_it(0, 1);
      push_it(-1, 0);
      push_it(0, -1);
      push_it(1, 1);
      push_it(-1, -1);
      push_it(-1, 1);
      push_it(1, -1);
    }
    // Done thing.
    unordered_set<int> path;
    path.insert(end);
    int pre = previous[end];
    while (pre != end) {
      path.insert(pre);
      end = pre;
      pre = previous[pre];
    }
    for (int i = 0; i < W * H; ++i) {
      if (path.find(i) != path.end()) {
        putchar(' ');
      } else {
        putchar(nodes[i]);
      }
      if ((i + 1) % W == 0)
        putchar('\n');
    }
    putchar('\n');
  }
}

