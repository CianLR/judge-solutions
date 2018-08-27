#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

#define abs(a) ((a) < 0 ? -(a) : (a))

int ClosestTo(int N, int tot, const vector<int> &weights) {
  vector<int> guesses(1, 0);
  vector<bool> seen(tot, false);
  seen[0] = true;
  int closest = 0, closest_dist = N, curr = 0, d;
  for (size_t i = 0; i < weights.size(); ++i) {
    vector<int> g = guesses;
    for (auto &a : g) {
      curr = a + weights[i];
      if (!seen[curr]) {
        d = abs(N - curr);
        seen[curr] = true;
        if (d < closest_dist || (d == closest_dist && curr > closest))
          closest_dist = d, closest = curr;
        if (curr > N + closest_dist) continue;
        guesses.push_back(a + weights[i]);
      }
      if (curr == N) return N;
    }
  }
  return closest;
}

int main() {
  int N, tot;
  scanf("%d\n", &N);
  vector<int> weights(N);
  for (int i = 0; i < N; ++i) scanf("%d", &weights[i]), tot += weights[i];
  sort(weights.rbegin(), weights.rend());
  printf("%d\n", ClosestTo(1000, tot, weights));
}

