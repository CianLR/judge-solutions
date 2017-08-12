#include <stdio.h>

#include <unordered_map>

class UF {
 public:
  int GetRoot(int a) {
    if (parent.find(a) == parent.end()) {
      parent[a] = -1;
      size[a] = 1;
      return a;
    }
    int prev = -2;
    while (parent[a] != -1) {
      parent[prev] = parent[a];
      prev = a;
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

  std::unordered_map<int, int> size;
  std::unordered_map<int, int> parent;
};

int main() {
  int N, Q;
  UF uf;
  scanf("%d %d", &N, &Q);
  char *op = new char[2];
  int a, b;
  while (Q--) {
    scanf("%s %d %d", op, &a, &b);
    if (*op == '?') {
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

