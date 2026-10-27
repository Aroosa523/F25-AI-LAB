
# AI Lab: Minimax and Alpha-Beta Pruning

## Objective
To implement Minimax and Alpha-Beta Pruning,
count evaluated leaf nodes, and compare branch ordering.

## Files
- lab_minimax.py: Python implementation
- Lab_Minimax_Report.docx: Lab report

## How to Run
Run the following command in the terminal:

python lab_minimax.py

## Leaf Scores
[3, 5, 2, 9, 3, 5, 2, 9]

## Expected Root Value
Both algorithms return the same root value: 5.

## Conclusion
Minimax evaluates all leaves. Alpha-Beta can skip
some leaves without changing the Minimax root value.
The number of leaves evaluated depends on branch order.