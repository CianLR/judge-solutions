#include <vector>
#include <string>
#include <algorithm>
#include <iostream>

class Solution {
 public:
  bool isMatch(std::string s, std::string p) {
    visited = std::vector<std::vector<bool>>(
        s.length() + 1, std::vector<bool>(p.length() + 1));
    dfs(s, p);
    // printVisited(s, p);
    return visited.back().back();
  }

 private:
  void dfs(const std::string &s, const std::string &p, int si=0, int pi=0) {
    if (visited[si][pi]) return;
    visited[si][pi] = true;
    if (si == s.length() || pi == p.length()) {
      // Special case, we can keep looking if pi is star.
      if (pi < p.length() && p[pi] == '*') dfs(s, p, si, pi+1);
      return;
    }
    if (p[pi] == '*') {
        dfs(s, p, si, pi + 1);
        dfs(s, p, si + 1, pi);
    } else if (p[pi] == '?') {
        dfs(s, p, si + 1, pi + 1);
    } else if (p[pi] == s[si]) {
        dfs(s, p, si + 1, pi + 1);
    }
  }

  void printVisited(const std::string &s, const std::string &p) {
    std::cout << "  ";
    for (const auto c : p) {
      std::cout << c << ' ';
    }
    std::cout << '\n';
    for (int i = 0; i < s.length() + 1; ++i) {
      if (i < s.length()) { std::cout << s[i] << ' '; }
      else { std::cout << "  "; }
      for (auto b : visited[i]) {
        std::cout << b << ' ';
      }
      std::cout << '\n';
    }
  }

  std::vector<std::vector<bool>> visited;
};

int main() {
    Solution s;
    std::cout << s.isMatch("cb", "?b") << '\n';
}