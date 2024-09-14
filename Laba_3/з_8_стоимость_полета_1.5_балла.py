import heapq


def dijkstra(graph, start, end):
    dist = {i: float('inf') for i in graph}
    dist[start] = 0
    prior_queue = [(0, start)]

    while prior_queue:
        curr_dist, curr_v = heapq.heappop(prior_queue)

        if curr_dist > dist[curr_v]:
            continue

        for n, w in graph[curr_v].items():
            distance = curr_dist + w

            if distance < dist[n]:
                dist[n] = distance
                heapq.heappush(prior_queue, (distance, n))

    return dist[end] if dist[end] != float('inf') else -1


with open('input.txt', 'r', encoding='utf-8') as file_input, open('output.txt', 'w', encoding='utf-8') as file_output:
    n, m = map(int, file_input.readline().split())
    graph = {i: {} for i in range(1, n + 1)}

    for _ in range(m):
        u, v, w = map(int, file_input.readline().split())
        graph[u][v] = w

    start, end = map(int, file_input.readline().split())

    result = dijkstra(graph, start, end)
    file_output.write(str(result))
