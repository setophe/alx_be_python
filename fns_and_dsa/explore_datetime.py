from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime

def calculate_future_date(days):
    return datetime.now() + timedelta(days=days)

print(f"Current date and time: {display_current_datetime()}")
days = int(input("Enter the number of days: "))
print(f"Future date: {calculate_future_date(days)}")
