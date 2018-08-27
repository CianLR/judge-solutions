#include <stdio.h>

#include <complex>
#include <unordered_set>
#include <vector>

using namespace std;

#define MX 2147483647
#define HASH(c) (((c).imag() << 10) + (c).real())

template<typename T> using Vector2D = vector<vector<T>>;

unsigned int GetPaths(int N, const Vector2D<bool> &wall_grid) {
  Vector2D<unsigned int> path_grid(N, vector<unsigned int>(N));
  path_grid[0][0] = 1;
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      if (!wall_grid[i][j] || (i == 0 && j == 0))
        continue;
      if (i > 0) path_grid[i][j] += path_grid[i - 1][j];
      if (j > 0) path_grid[i][j] += path_grid[i][j - 1];
      path_grid[i][j] %= MX;
    }
  }
  return path_grid[N - 1][N - 1];
}

const vector<complex<int>> MOVES = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

vector<complex<int>> NextStates(int N, const complex<int> &st) {
  vector<complex<int>> nxt;
  for (const auto &move : MOVES) {
    auto m = st + move;
    if (0 <= m.real() && m.real() < N &&
        0 <= m.imag() && m.imag() < N)
      nxt.push_back(m);
  }
  return nxt;
}

bool IsPossible(int N, const Vector2D<bool> &wall_grid) {
  vector<complex<int>> stack = {{0, 0}};
  unordered_set<int> seen = {HASH(stack[0])};
  while (!stack.empty()) {
    auto point = stack.back();
    stack.pop_back();
    for (auto &nxt : NextStates(N, point)) {
      if (seen.find(HASH(nxt)) == seen.end() &&
          wall_grid[nxt.real()][nxt.imag()])
        stack.push_back(nxt);
        seen.insert(HASH(nxt));      
    }
  }
  return seen.find(HASH(complex<int>(N - 1, N - 1))) != seen.end();
}

int main() {
  int N;
  scanf("%d", &N);
  Vector2D<bool> wall_grid(N, vector<bool>(N));
  char *line = new char[N + 1];
  for (int i = 0; i < N; ++i) {
    scanf("%s", line);
    for (int j = 0; j < N; ++j) {
      wall_grid[i][j] = line[j] == '.';
    }
  }

  unsigned int paths = GetPaths(N, wall_grid);
  if (paths) {
    printf("%u\n", paths);
    return 0;
  }
  if (IsPossible(N, wall_grid)) {
    printf("THE GAME IS A LIE\n");
  } else {
    printf("INCONCEIVABLE\n");
  }
}

