#include <ctype.h>
#include <stdio.h>

#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

struct Node {
  Node() : count(0), children(28, nullptr) {}

  void Insert(const char *s, unordered_set<Node *> &commits) {
    commits.insert(this);
    if (*s == '\0') return;
    char c = CharToIndex(*s);
    if (!children[c]) children[c] = new Node();
    children[c]->Insert(s + 1, commits);
  }

  inline char CharToIndex(char c) {
    if (c == ' ') return 26;
    else if (c == '-') return 27;
    else if ('A' <= c && c <= 'Z') return c - 'A';
    return c - 'a';
  }

  int ShortestUniquePrefix(const char *s, int len=0) {
    if (count == 1) return len;
    else if (*s == '\0') return -1;
    char c = CharToIndex(*s);
    return children[c]->ShortestUniquePrefix(s + 1, len + 1);
  }

  int count;
  vector<Node *> children;
};

string ToUpper(const string &s, int start, int len) {
  string out;
  out.reserve(len);
  for (int i = start; i < start + len; ++i) {
    out += toupper(s[i]);
  }
  return out;
}

int main() {
  int T, N;
  vector<string> songs;
  char *song = new char[128];
  scanf("%d", &T);
  for (int c = 1; c <= T; ++c) {
    scanf("%d\n", &N);
    songs.clear();
    Node root;
    for (int i = 0; i < N; ++i) {
      scanf("%[^\n]\n", song);
      songs.push_back(song);
      unordered_set<Node *> commits;
      char *song_suff = song;
      while (*song_suff) root.Insert(song_suff++, commits);
      for (const auto &n : commits) n->count++;
    }
    printf("Case #%d:\n", c);
    for (int i = 0; i < N; ++i) {
      int shortest_suff = 1000;
      string shortest, cmp_shortest;
      for (int j = 0; j < (int)songs[i].size(); ++j) {
        int sh = root.ShortestUniquePrefix(songs[i].c_str() + j);
        if (sh >= 0 && sh <= shortest_suff) {
          cmp_shortest = ToUpper(songs[i], j, sh);
          if (sh < shortest_suff || cmp_shortest < shortest)
            shortest = cmp_shortest;
          shortest_suff = sh;
        }
      }
      if (shortest_suff != 1000)
        printf("\"%s\"\n", shortest.c_str());
      else
        printf(":(\n");
    }
  }
}

