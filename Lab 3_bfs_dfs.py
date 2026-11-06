from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['G'],
    'D': ['G'],
    'G': []
}


def bfs(start, goal):
    queue = deque([start])
    parent = {start: None}
    visited = []

    while queue:
        node = queue.popleft()

        if node == goal:
            break

        visited.append(node)

        for neighbor in graph[node]:
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)

    path = []
    if goal in parent:
        node = goal
        while node is not None:
            path.append(node)
            node = parent[node]
        path.reverse()

    if goal not in parent:
        return visited, []

    visited.append(goal)
    return visited, path


def dfs(start, goal):
    stack = [start]
    parent = {start: None}
    visited = []

    while stack:
        node = stack.pop()

        if node == goal:
            visited.append(node)
            break

        visited.append(node)

        # Reverse to process B before C
        for neighbor in reversed(graph[node]):
            if neighbor not in parent:
                parent[neighbor] = node
                stack.append(neighbor)

    path = []
    if goal in parent:
        node = goal
        while node is not None:
            path.append(node)
            node = parent[node]
        path.reverse()

    return visited, path


bfs_order, bfs_path = bfs('A', 'G')
dfs_order, dfs_path = dfs('A', 'G')

print("BFS Visited Order:", bfs_order)
print("BFS Path:", bfs_path)

print("DFS Visited Order:", dfs_order)
print("DFS Path:", dfs_path)