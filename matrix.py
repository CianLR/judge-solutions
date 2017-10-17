import sys

def mat_map(f, mat):
    return [list(map(f, row)) for row in mat]


def get_inverse(mat):
    det_recip = 1 / ((mat[0][0] * mat[1][1]) - (mat[1][0] * mat[0][1]))
    return mat_map(lambda x: int(x * det_recip), [
        [mat[1][1], -mat[0][1]],
        [-mat[1][0], mat[0][0]],
    ])


def main():
    lines = sys.stdin.readlines()
    for i in range(len(lines) // 3):
        x00, x01 = [int(x) for x in lines[i * 3].split()]
        x10, x11 = [int(x) for x in lines[(i * 3) + 1].split()]
        print("Case {}:".format(i + 1))
        for row in get_inverse([[x00, x01], [x10, x11]]):
            print(*row)

if __name__ == '__main__':
    main()

