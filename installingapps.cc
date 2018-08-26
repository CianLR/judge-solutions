#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

struct App {
  App(int ind, int down, int stor)
    : index(ind), download(down), storage(stor) {
    min_size = download > storage ? download : storage;
  }
  int index, download, storage, min_size;
};

bool WeirdSort(const App &a, const App &b) {
  return (a.storage - a.download) > (b.storage - b.download);
}

int dp[500][10001];
bool used[500][10001];

int main() {
  int N, C, d, s;
  scanf("%d %d\n", &N, &C);
  vector<App> apps;
  apps.reserve(N);
  for (int i = 0; i < N; ++i) {
    scanf("%d %d", &d, &s);
    apps.emplace_back(i + 1, d, s);
  }
  sort(apps.begin(), apps.end(), WeirdSort);
  
  // Init first row.
  for (int c = 0; c < apps[0].min_size; ++c) {
    dp[0][c] = 0;
    used[0][c] = false;
  }
  for (int c = apps[0].min_size; c <= C; ++c) {
    dp[0][c] = 1;
    used[0][c] = true;
  }
  // Generic case.
  for (int i = 1; i < N; ++i) {
    for (int c = 0; c < apps[i].min_size; ++c) {
      dp[i][c] = dp[i - 1][c];
      used[i][c] = false;
    }
    for (int c = apps[i].min_size; c <= C; ++c) {
      if (dp[i - 1][c - apps[i].storage] + 1 > dp[i - 1][c]) {
        dp[i][c] = dp[i - 1][c - apps[i].storage] + 1;
        used[i][c] = true;
      } else {
        dp[i][c] = dp[i - 1][c];
        used[i][c] = false; 
      }
    }
  }

  printf("%d\n", dp[N - 1][C]);
  if (!dp[N - 1][C]) return 0;
  int cap = C;
  for (int i = N - 1; i >= 0; --i) {
    if (used[i][cap]) {
      printf("%d ", apps[i].index);
      cap -= apps[i].storage;
    }
  }
  printf("\n");
}

