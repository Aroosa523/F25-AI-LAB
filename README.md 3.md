AI Lab Task 3: Graph Search Algorithms

1. Introduction

This lab implements five Artificial Intelligence search algorithms: Breadth-First Search (BFS), Depth-First Search (DFS), Depth-Limited Search (DLS), Iterative Deepening Depth-First Search (IDDFS), and Uniform Cost Search (UCS).

The purpose is to understand how these algorithms explore a graph, find a goal, and compare paths based on depth, number of edges, and travel cost.

2. Original Graph

The start node is A, and the goal node is G.

Graph edges

- A -> B
- A -> C
- B -> D
- B -> E
- C -> F
- E -> G

Graph representation

          A
         / \
        B   C
       / \   \
      D   E   F
          |
          G

This is the original graph for BFS, DFS, DLS, and IDDFS.

For the UCS experiment, an additional edge C -> G is added as required by Section 3.7 of the lab manual.

3. Project Files

File 1: lab3_bfs_dfs.py

This file implements BFS and DFS.

- BFS uses a queue to explore nodes level by level.
- DFS uses a stack to explore a branch deeply before backtracking.
- Both algorithms start at A and search for G.

File 2: lab3_depth_search.py

This file implements DLS and IDDFS.

- DLS searches up to a specified depth limit.
- IDDFS repeats DLS with increasing depth limits.
- The required depth limits are 1, 2, 3, and 4.

File 3: lab3_ucs.py — Uniform Cost Search

This file implements Uniform Cost Search (UCS) on the weighted graph.

- The original graph vertices and corridors are retained.
- An additional corridor C -> G is included as required by Section 3.7.
- The "best_cost" dictionary tracks the lowest known cost to each node.
- A priority queue processes the path with the lowest accumulated cost first.
- The BFS alternative and UCS path are compared separately by number of edges and total cost.

Expected comparison:

- BFS alternative path: A -> C -> G
- BFS edge count: 2
- BFS total cost: 12
- UCS path: A -> B -> E -> G
- UCS edge count: 3
- UCS total cost: 3


4. How to Run the Programs

1. Open the project folder in Visual Studio Code.
2. Open "lab3_bfs_dfs.py" and click Run Python File.
3. Open "lab3_depth_search.py" and click Run Python File.
4. Open "lab3_ucs.py" and click Run Python File.
5. Check the output in the terminal.

Run each Python file separately.

5. Important Concepts

Queue: A FIFO data structure used by BFS.

Stack: A LIFO data structure used by DFS.

Depth limit: The maximum search depth allowed by DLS.

Iterative deepening: Repeated depth-limited searches with increasing limits.

Priority queue: A data structure used by UCS to process the lowest-cost option first.

Path cost: The sum of the weights of all edges in a path.

6. Expected Results

For the original graph, the expected path from A to G is:

A -> B -> E -> G

The goal is at depth 3.

For the weighted extension, the final UCS path and total cost depend on the reference weights specified in the lab manual. The results must be checked against those weights.

7. Conclusion

This lab demonstrates how different search algorithms find paths in graphs. BFS explores level by level, DFS explores branches deeply, DLS limits search depth, IDDFS increases the depth limit iteratively, and UCS finds a minimum-cost route in a weighted graph with non-negative edge costs.

8. Submission

The project includes the following files:

- "lab3_bfs_dfs.py"
- "lab3_depth_search.py"
- "lab3_ucs.py"
- "README.md"
- "Lab3_Report.docx"