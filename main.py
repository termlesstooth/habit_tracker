import json
from classes import Habit, HabitTracker


dev_habit = Habit("Habit Tracker Project", "Spend time contributing to habit tracker repo.", "d")
dev_habit.mark_completed()
print(dev_habit.name)

print(dev_habit.start_date)

data = {
    "Habit": dev_habit.name,
    "Description": dev_habit.description,
    "Frequency": dev_habit.frequency,
    "Start Date": str(dev_habit.start_date),
    "Current Streak": dev_habit.current_streak,
    "Completed Today": dev_habit.completed_today,
    "Completion Log": dev_habit.completion_log 
}

# write to a JSON file
with open('data/habits.json', 'w') as f:
    json.dump(data, f)

# # open the JSON file
# with open('habits.json') as f:
#     data = json.load(f)

# print(data)