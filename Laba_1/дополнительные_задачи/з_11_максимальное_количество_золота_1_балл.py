def knapsack(w, wi, n):
    value = [[0] * (w + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if j < wi[i - 1]:
                value[i][j] = value[i - 1][j]
            else:
                value[i][j] = max(value[i - 1][j], value[i - 1][j - wi[i - 1]] + wi[i - 1])
    return value[-1][-1]


with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w', encoding='utf-8') as output_file:
    w, n = map(int, input_file.readline().split())
    wi = [int(i) for i in input_file.readline().split()]
    output_file.write(str(knapsack(w, wi, n)))
