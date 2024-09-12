def min_refills(x, d, m, n):
    x = [0] + x + [d]

    num_refills = 0
    current_refill = 0
    while current_refill <= n:
        last_refill = current_refill

        while current_refill <= n and x[current_refill + 1] - x[last_refill] <= m:
            current_refill += 1

        if last_refill == current_refill:
            return -1

        if current_refill <= n:
            num_refills += 1

    return num_refills


with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w', encoding='utf-8') as output_file:
    d, m, n = int(input_file.readline()), int(input_file.readline()), int(input_file.readline())
    stop = [int(i) for i in input_file.readline().split()]
    output_file.write(str(min_refills(stop, d, m, n)))
