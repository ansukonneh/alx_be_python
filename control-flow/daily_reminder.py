task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

if priority == "high":
    message = f"Reminder: '{task}' is a high priority task"
elif priority == "medium":
    message = f"Reminder: '{task}' is a medium priority task"
elif priority == "low":
    message = f"Reminder: '{task}' is a low priority task"
else:
    message = f"Reminder: '{task}' has an unspecified priority"

if time_bound == "yes":
    if priority in ("high", "medium"):
        message += " that requires immediate attention today!"
    elif priority == "low":
        message += ", but it's time-sensitive so consider doing it soon."
    else:
        message += " and may require timely attention."
else:
    if priority == "low":
        message += ". Consider completing it when you have free time."
    else:
        message += "."

print(f"{message}")

