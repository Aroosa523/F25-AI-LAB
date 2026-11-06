def check_application(score, documents_complete, attendance, age):
    if score < 70:
        return "FAIL", "Score is below 70"
    if not documents_complete:
        return "FAIL", "Documents are incomplete"
    if attendance < 75:
        return "FAIL", "Attendance is below 75%"
    if age < 18:
        return "FAIL", "Age is below 18"
    return "PASS", "All conditions are satisfied"
# Four core test cases
test_cases = [
    ("Case 1", 80, True, 90, 20, "PASS"),
    ("Case 2", 80, True, 70, 20, "FAIL"),
    ("Case 3", 80, True, 90, 17, "FAIL"),
    ("Case 4", 70, True, 75, 18, "PASS")
]
for name, score, docs, attendance, age, expected in test_cases:
    actual, reason = check_application(
        score, docs, attendance, age
    )
    print(name)
    print("Input:", score, docs, attendance, age)
    print("Expected result:", expected)
    print("Actual result:", actual)
    print("Reason:", reason)
    print("-" * 40)
