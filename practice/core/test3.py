def gen_list(l):
    n = len(l)
    cl = len(l[0])
    res = [0] * cl
    for i in range(n):
        for j in range(cl):
            if not res[j]:
                res[j] = [None] * n
            res[j][i] = l[i][j]

    return res


if __name__ == '__main__':
    l = gen_list([[1, 2, 3, 109, 3],
                  [4, 5, 6, 22, 4],
                  [7, 8, 9, 78, 3],
                  [12, 13, 14, 15, 4]])
    print (l)

    # [1,4,7,12]
    # [2,5,6,22] l i = 0,j=1. res i=1,j= 0
    # [7,8,9,78]
    # [12,13,14,15] res [j][i]
