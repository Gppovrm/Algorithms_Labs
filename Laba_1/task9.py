def calculate_tariff(n, a):
    a = [[10 ** i, a[i]] for i in range(len(a))]
    a = sorted(map(lambda x: [x[0], x[1], x[1] / x[0]], a), key=lambda x: x[2])
    # print(a)
    tariff_one, tariff_parts = 2 * 10 ** 9 + 1, 0

    parts_n = n
    for i in a:
        if i[0] > n and i[1] < tariff_one:
            tariff_one = i[1]
            continue
        while parts_n >= i[0]:
            parts_n -= i[0]
            tariff_parts += i[1]

    return min(tariff_one, tariff_parts)


if __name__ == '__main__':
    with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w',
                                                                      encoding='utf-8') as output_file:
        n = int(input_file.readline())
        # a = sorted(map(lambda x: [x[0], x[1], x[1] / x[0]],
        #                [[10 ** i, int(input_file.readline())] for i in range(7)]), key=lambda x: x[2])
        a = [int(line.strip()) for line in input_file]
        output_file.write(str(calculate_tariff(n, a)))
