def all_paths_source_target(graph):
    n = len(graph)
    result = []

    def dfs(node, path):
        if node == n - 1:
            result.append(path[:])
            return

        for neighbor in graph[node]:
            dfs(neighbor, path + [neighbor])

    dfs(0, [0])
    return result

# Test cases
graph1 = [[1, 2], [3], [3], []]
print(all_paths_source_target(graph1)) 

graph2 = [[4, 3, 1], [3, 2, 4], [3], [4], []]
print(all_paths_source_target(graph2))