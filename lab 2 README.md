# Lab 2: Smart Room Temperature Control

## Project Description
This project is a simple Python program that simulates a smart room temperature control system. It checks the room temperature and occupancy status to decide whether the system should heat, cool, remain normal, or turn off.

The program also remembers the previous mode to determine whether a new command is required.

## Objectives
- To understand the use of Python functions.
- To use conditional statements.
- To understand global variables.
- To implement simple memory using the previous mode.
- To test temperature boundaries and room occupancy.

## Working of the Program

The system follows these rules:

- **OFF:** If the room is not occupied.
- **HEAT:** If the temperature is below 18°C.
- **COOL:** If the temperature is above 28°C.
- **NORMAL:** If the temperature is between 18°C and 28°C, including both boundaries.

The program compares the target mode with the previous mode.

- If the mode changes, it displays `Send command`.
- If the mode remains the same, it displays `No command`.

## Technologies Used
- Python 3
- Visual Studio Code (VS Code)

## Test Cases

The program includes six test cases:

| Test Case | Temperature | Occupied | Expected Mode |
|---|---:|---|---|
| Case 1 | 15°C | True | HEAT |
| Case 2 | 15°C | True | HEAT |
| Case 3 | 18°C | True | NORMAL |
| Case 4 | 28°C | True | NORMAL |
| Case 5 | 30°C | True | COOL |
| Case 6 | 25°C | False | OFF |

These test cases check heating, cooling, normal temperature, room occupancy, and repeated inputs.

## How to Run the Program

1. Install Python on your computer.
2. Open the project folder in VS Code.
3. Open the `lab 2 .py` file.
4. Open the terminal in VS Code.
5. Run the following command:

```bash
python "lab 2 .py"
```

## Expected Output
The program displays:
- Previous mode
- Current temperature
- Room occupancy status
- Target mode
- Command outcome

## Conclusion
This project demonstrates how a smart room temperature control system can make decisions using temperature and occupancy information. It also shows how a program can remember its previous mode and avoid sending unnecessary commands when the mode remains unchanged.