def dfs_cycle(graph, u, visited, visited_stack):
    visited[u] = True
    visited_stack[u] = True

    for node in graph[u]:
        if not visited[node]:
            if dfs_cycle(graph, node, visited, visited_stack):
                return True
        elif visited_stack[node]:
            return True

    visited_stack[u] = False
    return False


with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w", encoding='utf-8') as output_file:
    n, m = map(int, input_file.readline().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input_file.readline().split())
        graph[u - 1].append(v - 1)

    visited = [False for _ in range(n)]
    visited_stack = [False for _ in range(n)]

    for node in range(n):
        if not visited[node] and dfs_cycle(graph, node, visited, visited_stack):
            output_file.write('1')
            break
    else:
        output_file.write('0')
