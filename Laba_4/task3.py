def rabin_karp(p: str, t: str) -> list[int]:
    len_p, len_t = len(p), len(t)
    if len_p > len_t:
        return []

    result = []
    p_hash, t_hash = hash(p), hash(t[:len_p])

    for i in range(len_t - len_p + 1):
        if p_hash == t_hash:
            if p == t[i:i + len_p]:
                result.append(i + 1)
        if i < len_t - len_p:
            t_hash = hash(t[i + 1:i + len_p + 1])
    ans = f'{len(result)}\n{" ".join(map(str, result))}'
    return ans


def main():
    with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w",
                                                                      encoding='utf-8') as output_file:
        p, t = input_file.readline().strip(), input_file.readline().strip()
        ans = rabin_karp(p, t)
        output_file.write(ans)


if __name__ == '__main__':
    main()
