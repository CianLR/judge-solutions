#include <cstdio>

using namespace std;

int prices[2000];
int dp[21][2000];

inline int Round(int p) {
  int p10 = p % 10;
  return (p - p10) + (10 * (p10 >= 5));
}

int main() {
  int N, D;
  scanf("%d %d\n", &N, &D);
  for (int i = 0; i < N; ++i) {
    scanf("%d", &prices[i]);
  }
  int prev_sum = 0;
  for (int i = N - 1; i >= 0; --i) {
    prev_sum += prices[i];
    dp[0][i] = Round(prev_sum);
  }
  for (int d = 1; d <= D; ++d) {
    for (int start = 0; start < N; ++start) {
      int curr_price, min_price = dp[0][0], left_sum = 0;
      for (int i = start; i < N; ++i) {
        curr_price = Round(left_sum) + dp[d - 1][i];
        if (curr_price < min_price)
          min_price = curr_price;
        left_sum += prices[i];
      }
      dp[d][start] = min_price;
      if (d == D) break;
    }
  }
  printf("%d\n", dp[D][0]);
}

