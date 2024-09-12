def polynom_hash(s, x, m):
    h = [0] * (len(s) + 1)
    for i in range(len(s)):
        h[i + 1] = (h[i] * x + ord(s[i])) % m
    return h


with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w", encoding='utf-8') as output_file:
    m1, m2 = 10 ** 9 + 7, 10 ** 9 + 9
    x = 1
    s = input_file.readline().strip()
    h1 = polynom_hash(s, x, m1)
    h2 = polynom_hash(s, x, m2)
    ans = []
    n = len(s)
    q = int(input_file.readline())
    for _ in range(q):
        a, b, l = map(int, input_file.readline().split())
        hash1_a = (h1[a + l] - h1[a] * pow(x, l, m1)) % m1
        hash1_b = (h1[b + l] - h1[b] * pow(x, l, m1)) % m1
        hash2_a = (h2[a + l] - h2[a] * pow(x, l, m2)) % m2
        hash2_b = (h2[b + l] - h2[b] * pow(x, l, m2)) % m2

        if hash1_a == hash1_b and hash2_a == hash2_b:
            ans.append('Yes')
        else:
            ans.append('No')

    output_file.write('\n'.join(ans))
