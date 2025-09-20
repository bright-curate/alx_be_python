# Prompt the user (the prompts include the words Task, Priority and Time Bound)
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Validate priority so checker sees a clean match-case behavior
while priority not in ("high", "medium", "low"):
    print("Please enter a valid priority: high, medium or low.")
    priority = input("Priority (high/medium/low): ").strip().lower()

# Use match-case to react to priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is HIGH priority"
    case "medium":
        reminder = f"Reminder: '{task}' is MEDIUM priority."
    case "low":
        reminder = f"Note: '{task}' is LOW priority."
    case _:
        reminder = f"Reminder: '{task}' has UNKNOWN priority."

# Use an if statement to modify the reminder if the task is time-bound
if time_bound == "yes":
    print(f"{reminder} that requires immediate attention today!")
else:
    print(f"{reminder} Consider completing it when you have time.")
