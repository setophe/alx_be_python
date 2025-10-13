task = input("Enter your task: ")

# Ask for the priority level
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use a loop to make sure user enters valid priority
while priority not in ["high", "medium", "low"]:
    print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
    priority = input("Priority (high/medium/low): ").lower()

# Match-case statement for priority levels
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unspecified priority."

# Add condition for time sensitivity
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Print the customized reminder
print("\nReminder:", reminder)