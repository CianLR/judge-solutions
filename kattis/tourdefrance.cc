
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

int main() {
  int F, B;
  while (scanf("%d %d", &F, &B) == 2) {
    vector<int> front;
    int f;
    for (int i = 0; i < F; ++i) {
      scanf("%d", &f);
      front.push_back(f);
    }
    vector<int> back;
    int b;
    for (int i=0; i < B; ++i) {
      scanf("%d", &b);
      back.push_back(b);
    }

    vector<float> ratios;
    for (vector<int>::iterator it1 = front.begin(); it1 != front.end(); ++it1) {
      for (vector<int>::iterator it2 = back.begin(); it2 != back.end(); ++it2) {
        ratios.push_back(*it2 / float(*it1));
      }
    }

    sort(ratios.begin(), ratios.end());

    vector<float> other;
    for (int i = 1; i < ratios.size(); ++i)
      other.push_back(ratios[i] / ratios[i-1]);
  
    
    float biggest = 0;
    for (int i = 0; i < other.size(); ++i) {
      if (other[i] > biggest)
        biggest = other[i];
    }
    printf("%.2f\n", round(biggest * 100) / 100);

  }
  return 0;
}
