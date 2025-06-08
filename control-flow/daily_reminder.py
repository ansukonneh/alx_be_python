task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        priority_text = "a high priority task"
    case "medium":
        priority_text = "a medium priority task"
    case "low":
        priority_text = "a low priority task"
    case _:
        priority_text = "a task with unspecified priority"

# Determine urgency based on time-bound
if time_bound == "yes":
    if priority in ("high", "medium"):
        urgency_text = " that requires immediate attention today!"
    elif priority == "low":
        urgency_text = ", but it's time-sensitive so consider doing it soon."
    else:
        urgency_text = " and may require timely attention."
else:
    if priority == "low":
        urgency_text = ". Consider completing it when you have free time."
    else:
        urgency_text = "."
print(f"Reminder: '{task}' is {priority_text}{urgency_text}")
