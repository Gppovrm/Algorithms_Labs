def garland(n, a):
    n = int(n)
    lights_g = [0] * n
    lights_g[0] = a

    low, high = 0, a

    while high - low > 10 ** -12:
        lights_g[1] = (low + high) / 2
        flag_not_ground = True

        for i in range(1, n - 1):
            lights_g[i + 1] = 2 * lights_g[i] - lights_g[i - 1] + 2
            if lights_g[i + 1] < 0:
                flag_not_ground = False
                break

        if flag_not_ground:
            high = lights_g[1]
        else:
            low = lights_g[1]

    return round(lights_g[-1], 2)


def main():
    with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w',
                                                                      encoding='utf-8') as output_file:
        n, a = map(float, input_file.readline().split())

        result = garland(n, a)
        output_file.write(str(result))


if __name__ == '__main__':
    main()
