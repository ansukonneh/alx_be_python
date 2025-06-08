task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Required: match-case block
match priority:
    case "high":
        base_message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        base_message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        base_message = f"Reminder: '{task}' is a low priority task"
    case _:
        base_message = f"Reminder: '{task}' has an unspecified priority"

# Required: if-statement to modify message based on time-bound status
if time_bound == "yes":
    if priority in ("high", "medium"):
        base_message += " that requires immediate attention today!"
    elif priority == "low":
        base_message += ", but it's time-sensitive so consider doing it soon."
    else:
        base_message += " and may require timely attention."
else:
    if priority == "low":
        base_message += ". Consider completing it when you have free time."
    else:
        base_message += "."
print(base_message)
