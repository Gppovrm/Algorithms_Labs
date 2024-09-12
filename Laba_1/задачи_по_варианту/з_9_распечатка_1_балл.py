with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w', encoding='utf-8') as output_file:
    n = int(input_file.readline())
    a = sorted(map(lambda x: [x[0], x[1], x[1] / x[0]],
                        [[10 ** i, int(input_file.readline())] for i in range(7)]), key=lambda x: x[2])
    tariff_one, tariff_parts = 2 * 10 ** 9 + 1, 0

    parts_n = n
    for i in a:
        if i[0] > n and i[1] < tariff_one:
            tariff_one = i[1]
            continue
        while parts_n >= i[0]:
            parts_n -= i[0]
            tariff_parts += i[1]


    output_file.write(str(min(tariff_one, tariff_parts)))
