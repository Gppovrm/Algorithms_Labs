def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        else:  # i > r
            z[i] = 0
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            l, r = i, i + z[i] - 1
    return z[1:]

def main():
    with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w",
                                                                      encoding='utf-8') as output_file:
        s = input_file.readline().strip()
        result = z_function(s)
        output_file.write(' '.join(map(str, result)))

if __name__ == '__main__':
    main()
