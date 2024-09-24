task = input("Please input a task description: ")
priority = input("How important is the task (high, medium, low): ").lower()
time_bound = input("Are you time bound(yes or no): ")

match task:
    case task if priority == "high":
     print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
    case task if priority == "medium":
      print(f"Reminder: {task} task is due, please do allocate time to complete it later today.")
    case task if priority == "low":
     print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
