
# AI Lab: Minimax and Alpha-Beta Pruning

scores = [3, 5, 2, 9, 3, 5, 2, 9]
def build_tree(values):
    """Create a balanced binary tree from leaf scores."""
    if len(values) == 1:
        return values[0]

    mid = len(values) // 2
    return [
        build_tree(values[:mid]),
        build_tree(values[mid:])
    ]
tree = build_tree(scores)
def minimax(node, maximizing, counter):
    # A number represents a leaf node
    if isinstance(node, int):
        counter[0] += 1
        return node
    left = minimax(node[0], not maximizing, counter)
    right = minimax(node[1], not maximizing, counter)
    if maximizing:
        return max(left, right)
    else:
        return min(left, right)
def alpha_beta(node, maximizing, alpha, beta, counter):
    # A number represents a leaf node
    if isinstance(node, int):
        counter[0] += 1
        return node

    if maximizing:
        value = float('-inf')

        for child in node:
            value = max(
                value,
                alpha_beta(child, False, alpha, beta, counter)
            )
            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:
        value = float('inf')

        for child in node:
            value = min(
                value,
                alpha_beta(child, True, alpha, beta, counter)
            )
            beta = min(beta, value)

            if alpha >= beta:
                break

        return value


# Experiment 1: Original branch order
minimax_count = [0]
minimax_value = minimax(tree, True, minimax_count)

ab_count = [0]
ab_value = alpha_beta(
    tree, True, float('-inf'), float('inf'), ab_count
)

print("ORIGINAL BRANCH ORDER")
print("Minimax root value:", minimax_value)
print("Minimax leaves evaluated:", minimax_count[0])
print("Alpha-Beta root value:", ab_value)
print("Alpha-Beta leaves evaluated:", ab_count[0])


# Experiment 2: Reverse the branch order at every node
def reverse_tree(node):
    if isinstance(node, int):
        return node

    return [
        reverse_tree(node[1]),
        reverse_tree(node[0])
    ]
reordered_tree = reverse_tree(tree)

reordered_minimax_count = [0]
reordered_minimax_value = minimax(
    reordered_tree, True, reordered_minimax_count
)
reordered_ab_count = [0]
reordered_ab_value = alpha_beta(
    reordered_tree, True, float('-inf'), float('inf'),
    reordered_ab_count
)
print("\nREORDERED BRANCHES")
print("Minimax root value:", reordered_minimax_value)
print("Minimax leaves evaluated:",
    reordered_minimax_count[0])
print("Alpha-Beta root value:", reordered_ab_value)
print("Alpha-Beta leaves evaluated:", reordered_ab_count[0])