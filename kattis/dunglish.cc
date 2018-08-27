#include <stdio.h>
#include <vector>
#include <unordered_map>

using namespace std;

#define translate_map unordered_map<string, vector<string>>

long total_mappings(const vector<string> &sen,
                    const translate_map &cor,
                    const translate_map &incor) {
  unsigned int a, b;
  long maps = 1;
  for (auto &word : sen) {
    a = b = 0;
    if (cor.find(word) != cor.end())
      a = cor.find(word)->second.size();
    if (incor.find(word) != incor.end())
      b = incor.find(word)->second.size();
    maps *= a + b;
    if (maps == 0)
      return 0;
  }
  return maps;
}

void build_single_translate(const vector<string> &sen,
                            const translate_map &cor,
                            const translate_map &incor) {
  bool correct = true;
  for (auto &word : sen) {
    if (cor.find(word) != cor.end()) {
      printf("%s ", cor.find(word)->second[0].c_str());
      continue;
    }
    correct = false;
    printf("%s ", incor.find(word)->second[0].c_str());
  }
  if (correct)
    printf("\ncorrect\n");
  else
    printf("\nincorrect\n");
  return;
}

int main() {
  int N, M;
  scanf("%d", &N);
  vector<string> sentence;
  char dword[21], eword[21], type[21];
  for (int i = 0; i < N; ++i) {
    scanf("%s", dword);
    sentence.emplace_back(dword);
  }
  scanf("%d", &M);
  translate_map cor;
  translate_map incor;
  for (int i = 0; i < M; ++i) {
    scanf("%s %s %s", dword, eword, type);
    if (type[0] == 'c') {
      cor[dword].emplace_back(eword);
    } else {
      incor[dword].emplace_back(eword);
    }
  }
  long all_maps = total_mappings(sentence, cor, incor);
  if (all_maps == 1) {
    build_single_translate(sentence, cor, incor);
    return 0;
  }
  long correct_maps = total_mappings(sentence, cor, translate_map());
  printf("%ld correct\n", correct_maps);
  printf("%ld incorrect\n", all_maps - correct_maps);
  return 0;
}

