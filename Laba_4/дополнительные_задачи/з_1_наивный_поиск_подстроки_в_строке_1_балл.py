def are_equal(p: str, t: str) -> bool:
    if len(p) != len(t):
        return False
    for i in range(len(p)):
        if p[i] != t[i]:
            return False
    return True


def find_pattern_naive(p: str, t: str):
    res = []
    for i in range(len(t) - len(p) + 1):
        if are_equal(t[i: i + len(p)], p):
            res.append(str(i + 1))
    return res


with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w", encoding='utf-8') as output_file:
    p = input_file.readline().strip()
    t = input_file.readline().strip()
    ans = find_pattern_naive(p, t)
    output_file.write(f'{len(ans)}\n{" ".join(map(str, ans))}')
