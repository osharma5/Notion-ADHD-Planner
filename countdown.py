from datetime import datetime

deadline = "01-15-2026"
deadline_date = datetime.strptime(deadline, "%m-%d-%Y")
print("Days left:")
days_left = deadline_date - datetime.today()
print(days_left)