def longest_cycle(edges):
    n = len(edges)
    visited = [False] * n
    stack = [False] * n

    def dfs(node, count):
        visited[node] = True
        stack[node] = True

        next_node = edges[node]

        if not visited[next_node]:
            count = dfs(next_node, count + 1)
        elif stack[next_node]:
            count = max(count, 1)

        stack[node] = False
        return count

    result = -1

    for i in range(n):
        if not visited[i]:
            cycle_length = dfs(i, 0)
            if cycle_length > 1:
                result = max(result, cycle_length)

    return result

# Test cases
print(longest_cycle([3, 3, 4, 2, 3]))  
print(longest_cycle([2, -1, 3, 1]))
