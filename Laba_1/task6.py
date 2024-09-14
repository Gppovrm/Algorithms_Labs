def max_salary(x1, x2):
    if int(f'{x1}{x2}') > int(f'{x2}{x1}'):
        return True
    return False


def f_sort(l, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if max_salary(l[j + 1], l[j]):
                l[j + 1], l[j] = l[j], l[j + 1]


    return l



if __name__ == "__main__":
    with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w',
                                                                      encoding='utf-8') as output_file:
        n = int(input_file.readline())
        l = f_sort(input_file.readline().split(), n)
        ans = ''.join(l)
        output_file.write(ans)
