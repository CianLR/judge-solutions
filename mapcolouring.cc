#include <stdio.h>

#include <vector>

using namespace std;

bool ColourIsSafe(const vector<int> &adj, const vector<int> &colours, int c) {
  for (const auto &v : adj)
    if (colours[v] == c) return false;
  return true;
}

bool Colour(int C, const vector<vector<int>> &adj, vector<int> &colours, int c, int max_col) {
  if (c == C) return true;
  for (int col = 0; col < max_col; ++col) {
    colours[c] = col;
    if (ColourIsSafe(adj[c], colours, col) &&
        Colour(C, adj, colours, c + 1, max_col))
      return true;
  }
  colours[c] = -1;
  return false;
}

int MinColours(int C, const vector<vector<int>> &adj) {
  for (int m = 1; m <= 4; ++m) {
    vector<int> colours(C, -1);
    if (Colour(C, adj, colours, 0, m)) return m;
  }
  return -1;
}

int main() {
  int T, C, B, u, v;
  scanf("%d\n", &T);
  for (int t = 0; t < T; ++t) {
    scanf("%d %d\n", &C, &B);
    vector<vector<int>> adj(C);
    for (int b = 0; b < B; ++b) {
      scanf("%d %d\n", &u, &v);
      adj[u].push_back(v);
      adj[v].push_back(u);
    }
    int colours = MinColours(C, adj);
    if (colours == -1) printf("many\n");
    else               printf("%d\n", colours);
  }
}


