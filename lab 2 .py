
# Smart Room Temperature Control
previous_mode = None
def control_room(temperature, occupied):
    global previous_mode
    # Check the target mode
    if not occupied:
        target = "OFF"
    elif temperature < 18:
        target = "HEAT"
    elif temperature > 28:
        target = "COOL"
    else:
        target = "NORMAL"
    # Check if command is needed
    if target != previous_mode:
        command = "Send command"
    else:
        command = "No command"
    old_mode = previous_mode
    previous_mode = target
    return old_mode, target, command
# Test cases
tests = [
    (15, True),    # Heating
    (15, True),    # Same percept again
    (18, True),    # Exact lower boundary
    (28, True),    # Exact upper boundary
    (30, True),    # Cooling
    (25, False)    # Empty room
]
for temperature, occupied in tests:
    old, target, command = control_room(temperature, occupied)
    print("Previous Mode:", old)
    print("Percept:", temperature, "degrees, Occupied:", occupied)
    print("Target Mode:", target)
    print("Outcome:", command)
    print("--------------------")