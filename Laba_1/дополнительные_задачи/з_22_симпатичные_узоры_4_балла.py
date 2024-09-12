def checker(x, y, n):
    cell = [0] * 5

    for i in range(n - 1):
        cell[1] = 1 if (x // (2 ** i)) % 2 != 0 else 0
        cell[2] = 1 if (x // (2 ** (i + 1))) % 2 != 0 else 0
        cell[3] = 1 if (y // (2 ** i)) % 2 != 0 else 0
        cell[4] = 1 if (y // (2 ** (i + 1))) % 2 != 0 else 0

        if cell[1] == cell[2] == cell[3] == cell[4]:
            return False

    return True


def counter(n, m):
    res = 0
    length = 2 ** n  # количество всех возможных чисел длины n бит
    matrix = [[0] * length for _ in range(length)]
    s_dp = [[0] * length for _ in range(m)]

    for i in range(length):
        for j in range(length):
            if checker(i, j, n):
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

    for i in range(length):
        s_dp[0][i] = 1

    for k in range(1, m):
        for i in range(length):
            for j in range(length):
                s_dp[k][i] += s_dp[k - 1][j] * matrix[j][i]

    for i in range(length):
        res += s_dp[m - 1][i]

    return res


with open("INPUT.TXT", "r", encoding='utf-8') as input_file, open("OUTPUT.TXT", "w",
                                                                  encoding='utf-8') as output_file:
    n, m = sorted([int(i) for i in
                   input_file.readline().split()])  # чтоб точно знать какая на каком месте, из-за прохода циклов помогает уменьшить затраты памяти
    output_file.write(str(counter(n, m)))