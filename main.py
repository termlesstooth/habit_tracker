import json
from classes import Habit, HabitTracker
from datetime import date


# read in habits
with open('data/habit_tracker_object_backup.json', 'r') as f:
    data = json.load(f)


# store habits in habit tracker object
# TODO: can probably store the for loop as a method
all_habits = HabitTracker()
for habit in data:
    all_habits.add_habit(Habit.from_dict(habit))
print(all_habits.generate_report())

# write a new habit
python_dsa = Habit("Data Structures and Algorithms", "Solve Data Structures and Algorithms Python Problems","d")
all_habits.add_habit(python_dsa)

with open('data/habit_tracker_object.json', 'w') as f:
    json.dump(all_habits.convert_to_list_of_dicts(), f, indent=4)

# TODO: Need to write the habit tracker object to storage. Is the best way to do this with JSON Data or CSV. Complete that.
# TODO: Need to make it so that if I miss a day it automatically updates the log