#include <stdio.h>
#include <vector>

class UF {
 public:
  UF(int N) : size(N, 1), parent(N, -1) {
    for (int i = 0; i < N; ++i) parent[i] = i;
  }

  int GetRoot(int a) {
    while (parent[a] != a) {
      parent[a] = parent[parent[a]];
      a = parent[a];
    }
    return a;
  }

  bool Match(int a, int b) {
    return GetRoot(a) == GetRoot(b);
  }

  void Pair(int a, int b) {
    int ar = GetRoot(a), br = GetRoot(b);
    if (ar == br)
      return;
    if (size[ar] > size[br]) {
      parent[br] = ar;
      size[ar] += size[br];
    } else {
      parent[ar] = br;
      size[br] += size[ar];
    }
  }

  std::vector<int> size;
  std::vector<int> parent;
};

int main() {
  int N, Q;
  scanf("%d %d\n", &N, &Q);
  UF uf(N);
  char c;
  int a, b;
  while (Q--) {
    scanf("%c %d %d\n", &c, &a, &b);
    if (c == '?') {
      if (uf.Match(a, b))
        printf("yes\n");
      else
        printf("no\n");
    } else {
      uf.Pair(a, b);
    }
  }
  return 0;
}

