#include <stdio.h>

#include <string>
#include <vector>

using namespace std;

class Node {
 public:
  Node(char c=0) : c_(c), children_(26, nullptr) {}
 
  int Insert(const char *str) {
    if (*str == '\0') return 0;
    if (children_[*str - 'a']) {
      return 1 + children_[*str - 'a']->Insert(str + 1);
    }
    children_[*str - 'a'] = new Node(*str);
    children_[*str - 'a']->Insert(str + 1);
    return 0;
  }

 private:
  char c_;
  vector<Node *> children_;
};

int LCP(const vector<string> &strs) {
  int lcp = 0, l;
  Node root;
  for (const auto &s : strs) {
    l = root.Insert(s.c_str());
    if (l > lcp) lcp = l;
  }
  return lcp;
}

int main() {
  int R, C;
  scanf("%d %d\n", &R, &C);
  vector<string> transform(C, string(R, ' '));
  for (int r = 0; r < R; ++r) {
    for (int c = 0; c < C; ++c) {
      transform[c][R - (r + 1)] = getchar_unlocked();
    }
    getchar_unlocked();  // Newline.
  }
  printf("%d\n", R - (LCP(transform) + 1));
}

