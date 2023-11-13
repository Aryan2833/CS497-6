def minimum_cost(N, connections):
    parent = [i for i in range(N + 1)]

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1, root2 = find(node1), find(node2)
        if root1 != root2:
            parent[root1] = root2

    connections.sort(key=lambda x: x[2])

    total_cost = 0
    components = N

    for connection in connections:
        city1, city2, cost = connection
        if find(city1) != find(city2):
            union(city1, city2)
            total_cost += cost
            components -= 1

    return total_cost if components == 1 else -1

# Test cases
print(minimum_cost(3, [[1, 2, 5], [1, 3, 6], [2, 3, 1]]))
print(minimum_cost(4, [[1, 2, 3], [3, 4, 4]]))
