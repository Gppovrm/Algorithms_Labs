def max_lectures(lectures):
    lects = sorted(lectures, key=lambda x: x[1])
    counter = 1
    current_lec = lects[0]
    for i in lects[1:]:
        if i[0] >= current_lec[1]:
            current_lec = i
            counter += 1
    return counter


def main():
    with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w',
                                                                      encoding='utf-8') as output_file:
        n = int(input_file.readline())
        lects = [[int(i) for i in input_file.readline().split()] for _ in range(n)]
        output_file.write(str(max_lectures(lects)))


if __name__ == "__main__":
    main()
