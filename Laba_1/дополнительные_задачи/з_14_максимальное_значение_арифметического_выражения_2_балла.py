def MinAndMax(i, j, M, m, op):
    minimum = float("inf")
    maximum = float("-inf")
    for k in range(i, j):
        a = eval(f"{M[i][k]} {op[k]} {M[k + 1][j]}")
        # {op[k]} - на место {op[k]} встает один из знаков например - или *,еtсли op[k] равно +, то код выполнит сложение
        # динамически создает и выполняет выражение, исп. элементы матрицы и оператор из списка op
        b = eval(f"{M[i][k]} {op[k]} {m[k + 1][j]}")
        c = eval(f"{m[i][k]} {op[k]} {M[k + 1][j]}")
        d = eval(f"{m[i][k]} {op[k]} {m[k + 1][j]}")
        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    return minimum, maximum


def maxValue(d, op):
    n = len(d)
    m = [[0] * n for _ in range(n)]
    M = [[0] * n for _ in range(n)]

    # проходим по диагонали
    for i in range(n):
        m[i][i] = d[i]
        M[i][i] = d[i]
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j, M, m, op)
    return M[0][n - 1]


with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w", encoding='utf-8') as output_file:
    s = input_file.read().rstrip()
    digits = list(map(int, s[::2]))
    operators = list(s[1::2])

    output_file.write(str(maxValue(digits, operators)))


