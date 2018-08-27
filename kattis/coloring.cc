#include <stdio.h>
#include <stdlib.h>

#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

typedef vector<vector<int>> AdjList;

void find_safe(int node, const AdjList &lst, const vector<int> &colours, vector<bool> &is_safe) {
  for (size_t i = 0; i < lst[node].size(); ++i) {
    if (colours[lst[node][i]] != -1)
      is_safe[colours[lst[node][i]]] = false;
  }
}

bool colour(int node, const AdjList &lst, int max_colours, vector<int> &colours) {
  if (node >= lst.size())
    return true;
  vector<bool> is_safe(max_colours, true);
  find_safe(node, lst, colours, is_safe);
  for (int c = 0; c < max_colours; ++c) {
    if (!is_safe[c]) continue;
    colours[node] = c;
    if (colour(node + 1, lst, max_colours, colours))
      return true;
  }
  colours[node] = -1;
  return false;
}

void get_ints(char *line, vector<int> &out) {
  // Truly disgusting
  int i = -1;
  while (*line != 0) {
    if (48 > *line || 57 < *line) {
      if (i != -1) {  
        out.push_back(i);
        i = -1;
      }
      ++line;
      continue;
    }
    if (i == -1) i = 0;
    i = (i * 10) + (*line - '0');
    ++line;
  }
  if (i != -1)
    out.push_back(i);
  return;
}

int main() {
  int N;
  scanf("%d\n", &N);
  AdjList lst(N);
  int a, b;
  char line[256];
  for (int i = 0; i < N; ++i) {
    gets(line);
    get_ints(line, lst[i]);
  }

  for (int num_col = 1; num_col <= N; ++num_col) {
    vector<int> colours(N, -1);
    if (colour(0, lst, num_col, colours)) {
      printf("%d\n", num_col);
      break;
    }
  }  
}

