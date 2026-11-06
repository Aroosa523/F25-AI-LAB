import heapq

# Weighted graph for the UCS experiment
graph = {
    "A": [("B", 1), ("C", 2)],
    "B": [("D", 2), ("E", 1)],
    "C": [("F", 3), ("G", 10)],
    "D": [],
    "E": [("G", 1)],
    "F": [],
    "G": []
}


def ucs(start, goal):
    priority_queue = [(0, start, [start])]
    best_cost = {start: 0}
    processed = []

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        # Skip an outdated, more expensive path
        if cost > best_cost.get(node, float("inf")):
            continue

        processed.append(node)

        if node == goal:
            return path, cost, processed

        for neighbor, weight in graph[node]:
            new_cost = cost + weight

            if new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost
                heapq.heappush(
                    priority_queue,
                    (new_cost, neighbor, path + [neighbor])
                )

    return [], None, processed


# Run UCS from A to G
path, cost, processed = ucs("A", "G")

print("UCS Path:", path)
print("UCS Total Cost:", cost)
print("UCS Processed Nodes:", processed)

# Compare with the required BFS alternative
bfs_path = ["A", "C", "G"]
bfs_cost = 12

print("\nBFS Alternative Path:", bfs_path)
print("BFS Number of Edges:", len(bfs_path) - 1)
print("BFS Total Cost:", bfs_cost)

print("\nUCS Number of Edges:", len(path) - 1)
print("UCS Total Cost:", cost)