from collections import defaultdict, deque

def validPath(n, edges, source, destination):
    graph = defaultdict(list)

    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    queue = deque([source])

    while queue:
        current = queue.popleft()

        if current == destination:
            return True

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)

    return False

# Test cases
print(validPath(3, [[0,1],[1,2],[2,0]], 0, 2)) 
print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5)) 
