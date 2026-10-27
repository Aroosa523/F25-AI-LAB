# AI Lab 1 – Scholarship Eligibility Checker
## Project Description
This project is a simple Python program that checks whether a student is eligible for a scholarship based on four conditions: score, document completion, attendance, and age.

## Eligibility Criteria
The student must meet all the following conditions:

- **Score:** At least 70
- **Documents:** All required documents must be complete.
- **Attendance:** At least 75%
- **Age:** At least 18 years

If all conditions are satisfied, the application passes. Otherwise, the program returns a failure message explaining the reason.

## Technologies Used
- Python 3
- VS Code

## How to Run the Program

1. Install Python on your computer.
2. Open the project folder in VS Code.
3. Open the `AI LAB 1.PY` file.
4. Run the program using the Run button or terminal.

Run the following command in the terminal:

```bash
python "AI LAB 1.PY"
```

## Test Cases

The program includes four test cases:

| Test Case | Score | Documents Complete | Attendance | Age | Expected Result |
|---|---:|---|---:|---:|---|
| Case 1 | 80 | Yes | 90% | 20 | PASS |
| Case 2 | 80 | Yes | 70% | 20 | FAIL |
| Case 3 | 80 | Yes | 90% | 17 | FAIL |
| Case 4 | 70 | Yes | 75% | 18 | PASS |

## Expected Output
The program displays the following information for each test case:

- Test case name
- Input values
- Expected result
- Actual result
- Reason for passing or failing

## Conclusion
This project demonstrates the use of Python functions, conditional statements, return values, and test cases to check scholarship eligibility.

The program also tests boundary values, such as a score of 70, attendance of 75%, and age of 18.