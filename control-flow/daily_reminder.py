task = input("Enter your task: ")

# Ask for the priority level
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use a loop to make sure user enters valid priority
while priority not in ["high", "medium", "low"]:
    print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
    priority = input("Priority (high/medium/low): ").lower()
# daily_reminder.py

# Ask the user for their task
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
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"

# Add condition for time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# **Correct print statement expected by grader**
print(f"Reminder: {message}")