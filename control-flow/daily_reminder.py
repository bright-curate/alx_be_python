# Prompt user for task details
task = input("Enter your task for today: ")
priority = input("Enter the priority (high/medium/low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Use match case for priority
match priority:
    case "high":
        reminder = f"Your task '{task}' is HIGH priority."
    case "medium":
        reminder = f"Your task '{task}' is MEDIUM priority."
    case "low":
        reminder = f"Your task '{task}' is LOW priority."
    case _:
        reminder = f"Your task '{task}' has an UNKNOWN priority."

# Add time-sensitivity check
if time_bound == "yes":
    reminder += " It requires immediate attention today!"

# Final reminder
print("\n=== DAILY REMINDER ===")
print(reminder)
