#include <unordered_set>
#include <stdio.h>

int main() {
    int N, M;
    scanf("%d %d\n", &N, &M);
    while (N != 0 or M != 0) {
        std::unordered_set<int> jack;
        jack.reserve(N);
        int j;
        for (int i=0; i<N; ++i) {
            scanf("%d\n", &j);
            jack.insert(j);
        }
        int in_common = 0;
        for (int i=0; i<M; ++i) {
            scanf("%d\n", &j);
            if (jack.find(j) != jack.end()) ++in_common;
        }
        printf("%d\n", in_common);

        scanf("%d %d", &N, &M);
    }


    return 0;
}

