# def unit_cost_sort(l):
#     return l.sort(key=lambda x: x[0] / x[1], reverse=True)
#
#
# with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w", encoding='utf-8') as output_file:
#     n, w = map(int, input_file.readline().split())
#     items = [[int(j) for j in input_file.readline().split()] for _ in range(n)]
#
#     unit_cost_sort(items)
#
#     total = 0
#     i = 0
#     while w > 0:
#         if i == n:
#             break
#         elif items[i][1] <= w:
#             w -= items[i][1]
#             total += items[i][0]
#             i += 1
#         else:
#             total += (items[i][0] / items[i][1]) * w
#             w = 0
#
#     output_file.write(str(round(total, 4)))
def unit_cost_sort(l):
    l.sort(key=lambda x: x[0] / x[1], reverse=True)


def knapsack(n, w, items):
    unit_cost_sort(items)
    total = 0
    i = 0
    while w > 0:
        if i == n:
            break
        elif items[i][1] <= w:
            w -= items[i][1]
            total += items[i][0]
            i += 1
        else:
            total += (items[i][0] / items[i][1]) * w
            w = 0
    return round(total, 4)


if __name__ == "__main__":
    with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w",
                                                                      encoding='utf-8') as output_file:
        n, w = map(int, input_file.readline().split())
        items = [[int(j) for j in input_file.readline().split()] for _ in range(n)]
        result = knapsack(n, w, items)
        output_file.write(str(result))
