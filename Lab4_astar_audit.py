
import heapq
from itertools import count

# Graph: neighbour and travel cost
graph = {
    "S": {"A": 1, "B": 4},
    "A": {"C": 2},
    "B": {"G": 5},
    "C": {"G": 3},
    "G": {}
}

# Original heuristic values
h = {
    "S": 5,
    "A": 4,
    "B": 4,
    "C": 2,
    "G": 0
}
def search(use_heuristic=True):
    start = "S"
    goal = "G"
    # Queue items: (priority, tie_breaker, node, path_cost, path)
    queue = []
    order = count()
    start_h = h[start] if use_heuristic else 0
    heapq.heappush(
        queue, (start_h, next(order), start, 0, [start])
    )
    best_g = {start: 0}
    expanded = []
    name = "A*" if use_heuristic else "UCS"
    print("\n---", name, "SEARCH ---")

    while queue:
        f, _, node, g, path = heapq.heappop(queue)

        # Ignore an outdated queue entry
        if g != best_g.get(node):
            continue

        hn = h[node] if use_heuristic else 0

        print("Selected:", node,
            "g =", g, "h =", hn, "f =", f)

        # Goal is selected, but not counted as expanded
        if node == goal:
            print("Path:", " -> ".join(path))
            print("Path cost:", g)
            print("Expanded nodes:", expanded)
            print("Expansion count:", len(expanded))
            return path, g

        expanded.append(node)

        for neighbour, cost in graph[node].items():
            new_g = g + cost

            if new_g < best_g.get(neighbour, float("inf")):
                best_g[neighbour] = new_g

                new_h = h[neighbour] if use_heuristic else 0
                new_f = new_g + new_h
                new_path = path + [neighbour]

                heapq.heappush(
                    queue,
                    (new_f, next(order), neighbour,
                    new_g, new_path)
                )

    print("No path found.")
    return None, None


# Task 2: A* and UCS
search(True)
search(False)

# Task 3: Change only h(C)
print("\n--- OVERESTIMATION EXPERIMENT ---")
h["C"] = 10
search(True)