#include "stdio.h"
#include "stdint.h"

int times_in_q4(uint64_t x, uint64_t y, uint64_t grid_size) {
    if (grid_size == 1) return 0;
    uint64_t grid_sub = grid_size / 2;
    if (x >= grid_sub && y >= grid_sub) {
        return 1 + times_in_q4(x % grid_sub, y % grid_sub, grid_sub);
    } else {
        return times_in_q4(x % grid_sub, y % grid_sub, grid_sub);
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i=0; i<T; ++i) {
        int W, H;
        uint64_t X, Y, N;
        scanf("%ld %ld %ld %d %d", &N, &X, &Y, &W, &H);

        for (uint64_t y=Y; y < Y + H; ++y) {
            for (uint64_t x=X; x < X + W; ++x) {
                if (times_in_q4(x, y, N) % 2 == 0) printf("1");
                else printf("-1");
                if (x - X != W - 1) printf(" "); 
            }
            printf("\n");
        }
        printf("\n");
    }

    return 0;
}
