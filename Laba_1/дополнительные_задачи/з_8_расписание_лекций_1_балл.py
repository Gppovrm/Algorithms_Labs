with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w', encoding='utf-8') as output_file:
    n = int(input_file.readline())
    lects = sorted([[int(i) for i in input_file.readline().split()] for _ in range(n)], key=lambda x: x[1])
    # print(lects) -- сортируем по времени окончания
    counter = 1
    current_lec = lects[0]
    for i in lects[1:]:
        if i[0] >= current_lec[1]:
            current_lec = i
            counter += 1
    output_file.write(str(counter))
