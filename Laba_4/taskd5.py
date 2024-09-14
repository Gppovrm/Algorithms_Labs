def prefix_function(t):
    p = [0] * len(t)
    k = 0
    for i in range(1, len(t)):
        while k > 0 and t[k] != t[i]:
            k = p[k - 1]
        if t[k] == t[i]:
            k += 1
        p[i] = k
    return p


def KMP(s, t):
    p = prefix_function(t)
    result = []
    i, j = 0, 0
    while i < len(s):
        if s[i] == t[j]:
            i += 1
            j += 1
        if j == len(t):
            result.append(i - j)
            j = p[j - 1]
        elif i < len(s) and s[i] != t[j]:
            if j != 0:
                j = p[j - 1]
            else:
                i += 1
    return result

def main():
    with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w", encoding='utf-8') as output_file:
        s, t = input_file.readline().strip(), input_file.readline().strip()
        result = KMP(s, t)
        output_file.write(" ".join(map(str, result)))
if __name__ == '__main__':
    main()
