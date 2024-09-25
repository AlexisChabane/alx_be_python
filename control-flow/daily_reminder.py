task = input("Enter your task: ")
time_bound = input("Is it time-bound(yes/no): ")
priority = input("Priority (high/medium/low): ").lower(),

match priority:
    case priority if priority == "high":
      print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
    case priority if priority == "medium":
      print(f"Reminder: {task} task is due, please do allocate time to complete it later today.")
    case priority if priority == "low":
     print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
