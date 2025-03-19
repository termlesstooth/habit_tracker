import json
from classes import Habit, HabitTracker
from datetime import date

# jack_habit = Habit("Work on Habit Tracker", "Contribute to habit tracker project code", "d",date(2025,3,9),completion_log={'2025-03-09': True})
# jack_habit.mark_completed()
# print(jack_habit.completion_log)

# read in habit tracking object
with open('data/habits_backup.json','r') as f:
    data = json.load(f)

jack_habit = Habit.from_dict(data)

# write to json
with open('data/habits.json', 'w') as f:
    json.dump(jack_habit.to_dict(), f)

# #test of writing a single habit to a JSON
# data = {
#     "name": jack_habit.name,
#     "description": jack_habit.description,
#     "frequency": jack_habit.frequency,
#     "start_date": str(jack_habit.start_date),
#     "current_streak": jack_habit.current_streak,
#     "completed_today": jack_habit.completed_today,
#     "completion_log": jack_habit.completion_log 
# }
# # write to a JSON file
# with open('data/habits.json', 'w') as f:
#     json.dump(data, f) 





# jack_habit.mark_completed()


# TODO: Need to write the habit tracker object to storage. Is the best way to do this with JSON Data or CSV. Complete that.
# TODO: Need to make it so that if I miss a day it automatically updates the log


# TODO: Probably need to set up a method to do this

# with open('data/habits.json', 'w') as f:
#     json.dump(jack_habit.to_dict(), f)
# test of writing a single habit to a JSON
# data = {
#     "name": jack_habit.name,
#     "description": jack_habit.description,
#     "frequency": jack_habit.frequency,
#     "start_date": str(jack_habit.start_date),
#     "current_streak": jack_habit.current_streak,
#     "completed_today": jack_habit.completed_today,
#     "completion_log": jack_habit.completion_log 
# }
# # write to a JSON file
# with open('data/habits.json', 'w') as f:
#     json.dump(data, f) 

