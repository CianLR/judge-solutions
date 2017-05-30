H, W, h, w = map(int, input().split())
image = [[int(x) for x in input().split()] for _ in range(H)]
kernel = [[int(x) for x in input().split()] for _ in range(h)]
flip_kern = [r[::-1] for r in kernel[::-1]]

finished_image = [[0] * (W - w + 1) for _ in range(H - h + 1)]
for r in range(H - h + 1):
    for c in range(W - w + 1):
        for kr in range(h):
            for kc in range(w):
                finished_image[r][c] += flip_kern[kr][kc] * image[r + kr][c + kc]

for row in finished_image:
    print(*row)
