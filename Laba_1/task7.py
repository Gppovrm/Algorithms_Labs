def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)


def max_shoes_count(k, t):
    quick_sort(t, 0, len(t) - 1)
    count = 0
    i = 0
    while i < len(t) and k >= t[i]:
        k -= t[i]
        count += 1
        i += 1
    return count


def main():
    with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w",
                                                                      encoding='utf-8') as output_file:
        k, n = map(int, input_file.readline().split())
        t = [int(i) for i in input_file.readline().split()]
        result = max_shoes_count(k, t)
        output_file.write(str(result))


if __name__ == "__main__":
    main()
