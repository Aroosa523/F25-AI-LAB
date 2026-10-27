graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['G'],
    'D': ['G'],
    'G': []
}


def dls(node, goal, limit, path, visited):
    visited.append(node)

    if node == goal:
        return "Success", path

    if limit == 0:
        if graph[node]:
            return "Cutoff", None
        return "Failure", None

    cutoff_found = False

    for neighbor in graph[node]:
        if neighbor not in path:
            status, result = dls(
                neighbor, goal, limit - 1,
                path + [neighbor], visited
            )

            if status == "Success":
                return status, result

            if status == "Cutoff":
                cutoff_found = True

    if cutoff_found:
        return "Cutoff", None

    return "Failure", None


def iddfs(start, goal, max_depth):
    for limit in range(max_depth + 1):
        visited = []
        status, path = dls(
            start, goal, limit, [start], visited
        )

        print("Limit:", limit)
        print("Status:", status)
        print("Visited:", visited)
        print("Path:", path)

        if status == "Success":
            return limit, path

    return None, None


print("DLS RESULTS")

for limit in range(1, 5):
    visited = []
    status, path = dls(
        'A', 'G', limit, ['A'], visited
    )
    print(
        "Limit:", limit,
        "| Status:", status,
        "| Path:", path
    )

print("\nIDDFS RESULTS")
iddfs('A', 'G', 4)