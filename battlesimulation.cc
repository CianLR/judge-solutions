#include <iostream>
#include <string>

using namespace std;

inline bool is_combo(const string &mst, int i) {
  return mst[i] + mst[i+1] + mst[i+2] == 'R' + 'B' + 'L';
}

int main() {
  string monster;
  getline(cin, monster);
  
  string out;
  int i = 0;
  while (i < monster.length()) {
    if (monster.length() - i > 2 && is_combo(monster, i)) {
      out += 'C';
      i += 3;
      continue;
    }
    switch (monster[i]) {
      case 'R':
        out += 'S';
        break;
      case 'B':
        out += 'K';
        break;
      case 'L':
        out += 'H';
        break;
    }
    i += 1; 
  }
  cout << out << '\n';
}

